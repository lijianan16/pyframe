#改成函数
import json
import re

import jsonpath

#提取值
def json_path(resdata,expr):
    return jsonpath.jsonpath(resdata, expr)

def replace_new(old_data,value):
    json_str = json.dumps(old_data)  # 转化为字符串
    result = re.findall(r"(?<=\{\{).*?(?=\}\})", json_str)
    if result:
        #str
        newdata = json_str.replace("{{" + result[0] + "}}", value)
        #字典
        return json.loads(newdata)
    else:
        return None
def getpara(para):
    p="?"
    for key,value in para.items():
        # print(key)
        # print(value)
        p+= str(key)+"="+str(value)+"&"
    #对p进行处理
    if(p[-1])=="&":
        return (p[:-1])
if __name__ == '__main__':
    # res= {'status_code': 200, 'response': {'changeserial': 'Gfdjjsvcx Ntxybesfy Pqikt', 'msg': '出票请求已收', 'orderid': 'TGT_S57DF452F401', 'ordernumber': 'EF411150', 'success': 'TRUE', 'transactionid': '5AEA6654C8B', 'qkey': 'e27cfdadb'}, 'times': 0.062431}
    # # print(json_path(res,"$.response.qkey"))
    # li = [
    #     {
    #         "method": "$.train_request_change",
    #         "check": None
    #     },
    #     {
    #         "transactionid": "$.transactionid",
    #         "check": "eq"
    #     }
    # ]
    #只要有一个None --actual 参数有误
    # -- false
    # for l in li :
    #    print(None in  l.values())
    json = {
        "qkey": "e27cfdadb",
        "method": "train_request_change",
        "reqtime": "20180503102041",
        "sign": "72e172c1114332e0f82bc5f3b296b333",
        "isChangeTo": False,
        "partnerid": "tclycom",
        "from_station_code": "",
        "from_station_name ": "苏州 ",
        "to_station_code ": "",
        "to_station_name ": "上海 ",
        "orderid ": "TGT_S93C2F2F317ECECF70542 ",
        "transactionid ": "5AEA6C4F3F1E1 ",
        "ordernumber ": "E120765683 ",
        "change_checi ": "D8805 ",
        "change_datetime ": "2018 - 05 - 0316: 35: 00 ",
        "change_zwcode ": "O ",
        "old_zwcode ": "O ",
        "ticketinfo": [{
            "passengersename": "王春梅 ",
            "passporttypeseid": "1",
            "passportseno": "6000000000000 ",
            "piaotype ": "1 ",
            "old_ticket_no ": "E120765683108005D "
        }, {
            "passengersename": "王春梅 ",
            "passporttypeseid": "1",
            "passportseno": "6000000000002",
            "piaotype ": "1 ",
            "old_ticket_no ": "E120765683108005D "
        }],
        "isasync ": "Y ",
        "callbackurl ": "http: //t12306.com/trainOrder/services/changeOrderNotify ",
                              "reqtoken ": "FT5AUA71F90005BB5U410542 "
    }

jpath1 = jsonpath.jsonpath(json,"$.ticketinfo[0].passengersename")
jpath2 = jsonpath.jsonpath(json,"$..passengersename")
jpath = jsonpath.jsonpath(json,"$.method")
print(jpath)