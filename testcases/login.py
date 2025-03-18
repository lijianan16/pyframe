# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import allure
# import pytest
#
# from common.files.fileyaml import ReadYaml
# from common.para.requestdata import BeginRequest
# from common.selfassert.checkresult import verifyres, result_status
# #
# # data = ReadYaml("/Users/tim/Desktop/test_pro/pyframe/testcases/login.py")
# testcases =data.cases()
# ids = [case["caseid"] for case in testcases]
# @allure.epic("用户功能")
# @allure.feature("用户模块")
# class TestLogin():
#     @allure.story("用户信息接口")
#     @pytest.mark.parametrize("testcase",testcases,ids = ids)
#     def test_login(self,testcase):
#         res = BeginRequest().request_start(testcase)
#         result = verifyres(res.json(),testcase["expected"],testcase["actual"])
#         status = result_status(result)
#         assert status == 1
#
# if __name__=="__main__":
#     pytest.main(["-s","login.py"])
#
#
