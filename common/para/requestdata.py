import redis
from pydantic import ValidationError

from common.para.redisutil import redisdata
from common.utils.Model import RequestData, Resposne
from common.utils.filterdata import replace_new, getpara, json_path
from common.utils.requestsession import RequestSess

redi = redisdata()

def request_keyword(reqdata):
    url = reqdata.url
    method = reqdata.method
    headers = reqdata.headers
    type = reqdata.type
    dependen = reqdata.dependen
    data = reqdata.data
    url = redi.getred("base_url")+url
    # 加判断条件
    kw = {}
    if type == "params":
        print(type)
        url += getpara(data)
        print(url)
    # if type == None and data==None:

    elif type == "data":
        kw["data"] = data
        kw["headers"] = headers
    elif type == "json":
        if dependen == None:
            kw["json"] = data
            kw["headers"] = headers
        else:
            if None in dependen.values():
                # 不需要替换
                kw["json"] = data
                kw["headers"] = headers
            else:
                print("执行替换参数操作")
                # 参数替换未做
                # print(redis.getred("qkey"))
                data = replace_new(data, redi.getred("qkey"))
                kw["json"] = data
                kw["headers"] = headers
    return method, url, kw

class BeginRequest(RequestSess,redisdata):
    def __init__(self):
        super().__init__()
    def request_start(self,testcase):
        try:
            reqdata = RequestData(**testcase)
            req_keyword = request_keyword(reqdata)
            print("**********")
            print(req_keyword)
            print("**********")
            extract = reqdata.extract
            actual = reqdata.actual

            res = self.httpreq(req_keyword[0], req_keyword[1], **req_keyword[2])
            response = self.result(res)
            print(response)
            # class
            res_check = Resposne(**response)
            res_dict = res_check.dict()
            # 取值之后
            if extract == None:
                print("不需执行提取")
            else:
                if None in extract.values():
                    print("value is None 不执行")
                else:
                    print(res_dict)
                    # 提取值
                    for key, value in extract.items():
                        print(value)
                        print(json_path(res_dict, value))
                        # 调用redis方法

                        redi.setred(key, json_path(res_dict, value)[0])
            # actual为列表类型
            # if actual == None:
            #     print("1、无期望值")
            # else:
            #     for l in actual:
            #         # pytest断言- allure
            #         print(l.items())
            # 实际值跟预期比较
            return res
        except(ValidationError) as e:
            print(e)
