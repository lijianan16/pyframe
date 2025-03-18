from typing import Dict, Text

import requests
from requests import JSONDecodeError

from common.para.redisutil import redisdata
from common.utils.logs import Logger

# log = Logger().get_logger()
class RequestSess(Logger):
    def __init__(self):
        self.req = requests.Session()
        self.redi = redisdata()

        super().__init__()
    def httpreq(self,method:Text,url:Text,**kwargs:Dict):
        token_value =  self.redi.getred("Authorization")
        # self.logger.info(token_value)
        print(token_value)
        if token_value !=None:  #try
            self.req.headers.update({"Authorization": self.redi.getred("Authorization")})
        res = self.req.request(method=method, url=url, **kwargs, timeout=(2, 3))
        self.logger.info(res.elapsed.total_seconds())
        if 200<= res.status_code <300:
             return res
        elif 300<= res.status_code <400:
            self.logger.error(
                f"statuscode:{res.status_code}_this request is 'choice error' url is :{url},method is:{method},body is :{kwargs}")
            # log.error(f"this request is error:{url},{method},{kwargs}")
            print("choice")
        elif 400<=res.status_code <500:
            # self.get_logger().error("test")
            self.logger.error(f"statuscode:{res.status_code}_this request is 'client error' url is :{url},method is:{method},body is :{kwargs}")
            # log.error(f"statuscode:{res.status_code}_this request is error url is :{url},method is:{method},body is :{kwargs}")
            print("client error")
        elif 500<= res.status_code <600:
            self.logger.error(
                f"statuscode:{res.status_code}_this request is 'server error' url is :{url},method is:{method},body is :{kwargs}")
            print("server error")
    #res 传进来
    #return:{'status_code': 200, 'response': {'code': 200, 'msg': 'success', 'data': {'pro': '增加成功'}}, 'times': 0.172719}
    def result(self,res):
        if res != None:
            return {"status_code":res.status_code,"response":res.json(),"times":res.elapsed.total_seconds()}
        else:
            return None


    def close(self):
        self.req.close()

if __name__ == '__main__':
    res =  RequestSess()
    header = {"Content-Type": "application/json"}
    kw = {"json": {"pro_no": "2299",
                   "pro_name": "大牛测试测试2299"}}
    kw1 = {"headers": header, **kw}

    # r = requests.Session().request(method="post",url=url,**kw)
    # print(r.json())
    # **不要少
    # url = "http://localhost:8000/aiplat/pro"
    #可变参数

    u = "http://rap2api.taobao.org/app/mock/126135/api/applyChange"
    h = {'Accept-Charset': 'UTF-8', 'Content-Type': 'application/json'}
    body = {"qkey": "adgase2","method": "train_request_change","reqtime": "20180503102041","sign": "72e172c1114332e0f82bc5f3b296b333","isChangeTo": False,"partnerid": "tclycom","from_station_code": "","from_station_name ": "苏州 ","to_station_code ": "","to_station_name ": "上海 ","orderid ": "TGT_S93C2F2F317ECECF70542 ","transactionid ": "5AEA6C4F3F1E1 ","ordernumber ": "E120765683 ","change_checi ": "D8805 ","change_datetime ": "2022 - 05 - 0316: 35: 00 ","change_zwcode ": "O ","old_zwcode ": "O ","ticketinfo ": [{"passengersename ": "王春梅 ","passporttypeseid ": "1 ","passportseno ": "6000000000000 ","piaotype ": "1 ","old_ticket_no ": "E120765683108005D "}],"isasync ": "Y ","callbackurl ": "http: //t12306.com/trainOrder/services / changeOrderNotify ","reqtoken ": "FT5AUA71F90005BB5U410542 "}
    kw ={"qkey": "qebebae@", "method": "train_request_change", "reqtime": "20180503102041", "sign": "72e172c1114332e0f82bc5f3b296b333", "isChangeTo": False, "partnerid": "tclycom", "from_station_code": "", "from_station_name ": "苏州 ", "to_station_code ": "", "to_station_name ": "上海 ", "orderid ": "TGT_S93C2F2F317ECECF70542 ", "transactionid ": "5AEA6C4F3F1E1 ", "ordernumber ": "E120765683 ", "change_checi ": "D8805 ", "change_datetime ": "2022 - 05 - 0316: 35: 00 ", "change_zwcode ": "O ", "old_zwcode ": "O ", "ticketinfo ": [{"passengersename ": "王 ", "passporttypeseid ": "1 ", "passportseno ": "6000000000000 ", "piaotype ": "1 ", "old_ticket_no ": "E120765683108005D "}], "isasync ": "Y ", "callbackurl ": "http: //t12306.com/trainOrder/services / changeOrderNotify ", "reqtoken ": "FT5AUA71F90005BB5U410542 "}
    pp = {'json': {"qkey": "qebebae@", "method": "train_request_change", "reqtime": "20180503102041", "sign": "72e172c1114332e0f82bc5f3b296b333", "isChangeTo": False, "partnerid": "tclycom", "from_station_code": "", "from_station_name ": "\\u82cf\\u5dde ", "to_station_code ": "", "to_station_name ": "\\u4e0a\\u6d77 ", "orderid ": "TGT_S93C2F2F317ECECF70542 ", "transactionid ": "5AEA6C4F3F1E1 ", "ordernumber ": "E120765683 ", "change_checi ": "D8805 ", "change_datetime ": "2022 - 05 - 0316: 35: 00 ", "change_zwcode ": "O ", "old_zwcode ": "O ", "ticketinfo ": [{"passengersename ": "\\u738b\\u6625\\u6885 ", "passporttypeseid ": "1 ", "passportseno ": "6000000000000 ", "piaotype ": "1 ", "old_ticket_no ": "E120765683108005D "}], "isasync ": "Y ", "callbackurl ": "http: //t12306.com/trainOrder/services / changeOrderNotify ", "reqtoken ": "FT5AUA71F90005BB5U410542 "}, 'headers': {'Accept-Charset': 'UTF-8', 'Content-Type': 'application/json'}}
    result = res.httpreq("post",u,**pp)
    print(result.json())
    # print(res.result(result))
    #None - 404 ,200 -300 正常。
    body = {
        "pro_no": "2299",
        "pro_name": "大牛测试测试2299"
    }
    #拆分
    #不拆分，注意key
    # result = res.httpreq("post1", url, json=body,headers=header)
    # res.result(result)
    # print(result.json())
    #status_code  405