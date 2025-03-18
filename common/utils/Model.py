from typing import Text, Dict, Union, List

from pydantic import BaseModel

from common.files.fileyaml import ReadYaml



#请求数据
class RequestData(BaseModel):
    name:Text
    url: Text
    method:Text
    headers:Dict
    cookie:Union[None,Dict]
    run:Text
    type:Union[Text,None]
    data:Union[Text,Dict,None]
    dependen:Union[None,Dict]
    extract:Union[None,Dict]
    actual:List
    expected:Dict
class Resposne(BaseModel):
    status_code:int
    response:Dict
    times:float


if __name__ == '__main__':
    r = ReadYaml("/Users/tim/Desktop/test_pro/pyframe/data/ticket.yml")
    # redis = redisdata()
    # data_all = r.read_yml_file()
    # http = RequestSess()
    # print(r.casename())
    #
    # for caseid in r.casename():
    #     if caseid != "config":
    #         print(caseid)
    #         print(data_all.get(caseid))
    #         #1、验证key，2、value类型，加上try 异常log
    #         try:
    #             reqdata = RequestData(**data_all.get(caseid))
    #             req_keyword = request_keyword(reqdata)
    #             print("**********")
    #             print(req_keyword)
    #             print("**********")
    #             extract = reqdata.extract
    #             actual = reqdata.actual
    #             res  =http.httpreq(req_keyword[0],req_keyword[1],**req_keyword[2])
    #             response = http.result(res)
    #             #class
    #             res_check = Resposne(**response)
    #             res_dict = res_check.dict()
    #             # 取值之后
    #             if extract == None:
    #                 print("不需执行提取")
    #             else:
    #                 if None in extract.values():
    #                     print("value is None 不执行")
    #                 else:
    #                     print(res_dict)
    #                     #提取值
    #                     for key,value in extract.items():
    #                         print(value)
    #                         print(json_path(res_dict,value))
    #                         #调用redis方法
    #                         redis.setred(key,json_path(res_dict,value)[0])
    #             #actual为列表类型
    #             if actual == None:
    #                 print("1、无期望值")
    #             else:
    #                 for l in actual:
    #                 #pytest断言- allure
    #                     print(l.items())
    #                     #实际值跟预期比较




                # for key in res_check.dict():
                #     print(key)
                #     print(res_va[key])
            #
            # except(ValidationError) as e:
            #     print(e)

