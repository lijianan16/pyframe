# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import allure
# import pytest
#
# from common.files.fileyaml import ReadYaml
# from common.para.requestdata import BeginRequest
# from common.selfassert.checkresult import verifyres, result_status
#
# data = ReadYaml("/Users/tim/Desktop/test_pro/pyframe/testcases/ticket.py")
# testcases =data.cases()
# ids = [case["caseid"] for case in testcases]
# @allure.epic("用户功能")
# @allure.feature("用户模块")
# class TestTicket():
#     @allure.story("用户信息接口")
#     @pytest.mark.parametrize("testcase",testcases,ids = ids)
#     def test_ticket(self,testcase):
#         res = BeginRequest().request_start(testcase)
#         result = verifyres(res.json(),testcase["expected"],testcase["actual"])
#         status = result_status(result)
#         assert status == 1
#
# if __name__=="__main__":
#     pytest.main(["-s","ticket.py"])
#
#
from common.base import pro_path
from common.utils.logs import Logger, log_time
#
# if __name__ == '__main__':
    # log = Logger().get_logger()
    # log.info("test")
    # log.error("test")
    # log.debug("test")
    # log.exception("test")
    # my_log_file_path = pro_path() + "logs/" + log_time + "test.log"
    # print(my_log_file_path)


