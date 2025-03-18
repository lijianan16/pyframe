# import pytest
# data =[{"user":"a","pwd":"bb"}]
# class TestTicket():
#     @pytest.mark.parametrize("test_data",data,ids =["login_1"])
#     def test_ticket(self,test_data):
#         print(test_data["user"])
#         print(test_data["pwd"])
# if __name__=="__main__":
#     pytest.main(["-s","test_ticket.py"])
from common.para.redisutil import redisdata

# redi = redisdata()
#
#
# def test_token(get_token):
#     print("***")
#     print(redi.getred("Authorization"))
#     print(redi.getred("base_url"))
#     print("***")