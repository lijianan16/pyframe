import os
import sys

import yaml

from common.utils.logs import Logger


class ReadYaml(Logger):
    def __init__(self,filepath):
        self.filepath = filepath
        super().__init__()
    def read_yml_file(self):
        try:
            file = open(self.filepath,"r",encoding="utf-8")
            ymlformat =yaml.safe_load(file)
            return ymlformat
        except(FileNotFoundError) as e:
            self.logger.exception(e)
    #返回用例名
    #前提yml文件数据正常
    #return ['config', 'loging_1', 'loging_2']
    def casename(self):
        casenamelist = []
        for key in  self.read_yml_file():
            casenamelist.append(key)
        return casenamelist

    def cases(self):
        cases = []
        data = self.read_yml_file()
        for key in data:
            if key != "config":
                #caseid
                case = data[key]
                case.update({"caseid":key})
                cases.append(case)
        return cases



if __name__ == '__main__':
    r = ReadYaml("/Users/tim/Desktop/test_pro/pyframe/data/ticket.yml")
    # data = ReadYaml("/Users/tim/Desktop/test_pro/pyframe/testcases/dept/test_deptinfo.py")"
    # data = r.read_yml_file()
    # print(data)
    # print(type(data))
    # print(r.cases())
    # print([case["caseid"] for case in r.cases()])
    #测试异常
    #思路-读出来之后-放到请求里面-结果-分析->写到报告里
    #excel读出来-str类型,yml直接是字典类型


