# 创建并写入Python模板文件
def new_python_template(filename,ymlfile,epic,feature, classname,story,test_name,pyfilename):
    print(filename)
    # 打开文件用于写入
    with open(filename, 'w') as file:
        # 写入模板内容
        file.write("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""")
        # 添加函数模板
        file.write(f"""import allure
import pytest

from common.files.fileyaml import ReadYaml
from common.para.requestdata import BeginRequest
from common.selfassert.checkresult import verifyres, result_status

data = ReadYaml("{ymlfile}")
testcases =data.cases()
ids = [case["caseid"] for case in testcases]
@allure.epic("{epic}")
@allure.feature("{feature}")
class Test{classname}():
    @allure.story("{story}")
    @pytest.mark.parametrize("testcase",testcases,ids = ids)
    def test_{test_name}(self,testcase):
        res = BeginRequest().request_start(testcase)
        result = verifyres(res.json(),testcase["expected"],testcase["actual"])
        status = result_status(result)
        assert status == 1

if __name__=="__main__":
    pytest.main(["-s","{pyfilename}"])


""")
# create_python_template('template.py', classname="Test2")