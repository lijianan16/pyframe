# _*_ coding:utf-8 _*_
from os.path import dirname
import sys,pytest

from common.base import pro_path
from common.utils.logs import log_time

path = dirname(__file__)
sys.path.append(path)
import pytest
import os
# from Common.function import projectPath

path = path+"/testcases/"
report =path+"reports/"
#写个方法，检测系统是win 还是mac
pytest.main(["-s", "--alluredir={}".format(report),
             path])  # 运行 cases下所有测试用例

result = os.system(r"allure serve {}".format(report))
# print(path)
if __name__ == '__main__':
    print(path)
    print(report)