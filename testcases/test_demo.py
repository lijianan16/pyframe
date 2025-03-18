# # # import allure
# # # @allure.feature("大牛测试")
# # # @allure.story("登录测试")
# # from common.para.redisutil import redisdata
# #
# # redi = redisdata()
# # class Testdn:
# #     def test_one(self,get_token):
# #         print("@@@")
# #         print(redi.getred("base_url"))
# #         print(redi.getred("Authorization"))
# #         print("@@@")
# #         print(get_token)
# #         # allure.dynamic.title("用户名测试")
# #         # a = "daniu"
# #         # assert a == "daniu"
# # #     def test_two(self):
# # #         allure.dynamic.title("登录按钮测试")
# # #         a = "daniu"
# # #         assert a == "daniu"
# from common.para.redisutil import redisdata
# from common.utils.filterdata import json_path
# from common.utils.requestsession import RequestSess
#
# http = RequestSess()
from common.para.redisutil import redisdata

# redi = redisdata()
# #
# def test_token(get_token):
#     print("***")
#     print(redi.getred("Authorization"))
#     print(redi.getred("base_url"))
#     print("***")
#     #登录-拿token值
#     body= {
#         "username": "admin",
#         "password": "admin123",
#         "code": "2",
#         "uuid": "4add4772db54492da56d5eb9d895322c"
#
#     }
#     redi.dele("Authorization")
#     res = http.httpreq("post","http://192.168.0.101:8080/login",json=body)
#     #异常
#     # print(res.json())
#     token = json_path(res.json(),"$.token")
#     print("_____")
#     print(token)
#     print("_____")
#     redi.setred("base_url",base_url)
#     redi.setred("Authorization","Bearer "+token[0])
#     print(redi.getred("Authorization"))
#     print(base_url)
#     # return res.json()