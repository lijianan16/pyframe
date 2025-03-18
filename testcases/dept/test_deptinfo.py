#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import allure
import pytest

from common.files.fileyaml import ReadYaml
from common.para.requestdata import BeginRequest
from common.selfassert.checkresult import verifyres, result_status

data = ReadYaml("/Users/tim/Desktop/test_pro/pyframe/data/dept/deptinfo.yml")
testcases =data.cases()
ids = [case["caseid"] for case in testcases]
@allure.epic("部门功能")
@allure.feature("部门模块")
class TestDeptinfo():
    @allure.story("部门信息接口")
    @pytest.mark.parametrize("testcase",testcases,ids = ids)
    def test_deptinfo(self,testcase):
        res = BeginRequest().request_start(testcase)
        result = verifyres(res.json(),testcase["expected"],testcase["actual"])
        status = result_status(result)
        assert status == 1

if __name__=="__main__":
    pytest.main(["-s","deptinfo.py"])


