import pytest

from common.para.redisutil import redisdata
from common.utils.filterdata import json_path
from common.utils.logs import Logger
from common.utils.requestsession import RequestSess

http = RequestSess()
redi = redisdata()
log = Logger().get_logger()
@pytest.fixture(scope="session",autouse=True)
def get_token(base_url):
    #登录-拿token值
    body= {
        "username": "admin",
        "password": "admin123",
        "code": "4",
        "uuid": "8944574faf7c491b91734ecf4f69c638"

    }
    redi.delred("Authorization")
    redi.delred("base_url")
    res = http.httpreq("post","http://192.168.0.101:8080/login",json=body)
    #异常
    # print(res.json())
    token = json_path(res.json(),"$.token")
    print("_____")
    print(token)
    print("_____")
    redi.setred("base_url",base_url)
    redi.setred("Authorization","Bearer "+token[0])
    log.info("Authorization:Bearer "+token[0])
    print(redi.getred("Authorization"))
    print(base_url)
    # return res.json()

#操作都用到token,先能正常登录
#没token,
#token哪边加进去- token /url 传过去
#redis,token、url
#登录-token