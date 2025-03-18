from os.path import dirname
import sys,pytest
path = dirname(__file__)
sys.path.append(path.split("testcases")[0])
import unittest,os
path = os.getcwd()
print(path)
# def allcase():
#     discover = unittest.defaultTestLoader.discover(path,'loginunittest.py',top_level_dir=None)
#     return discover
# runer = unittest.TextTestRunner()
# runer.run(discover)
pa = path.split("testcases")[0]+"testcases/"
report = path.split("testcases")[0]+"reports/"
print(pa)
print(report)
# pytest.main(["-s","--alluredir={}".format(report),path])
# result = os.system(r"allure serve {}".format(report))
# path = projectpath()+"testcases\\"
# report =projectpath()+"reports\\"
pytest.main(["-s", "--alluredir={}".format(report),
             pa])  # 运行 cases下所有测试用例

if __name__ == '__main__':
    # print(path.split("testcases")[0])
    # file_name =projectpath()+"reports\\"+"dn.html"
    # fp = open(file_name,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="dntest_report",description="web test")
    # runner.run(allcase())
    print(path)
    # print(report)