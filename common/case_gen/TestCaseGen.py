#取所有yml文件
import os
import pathlib

from common.case_gen.case_module import new_python_template
from common.files.fileyaml import ReadYaml





class TestCaseGener:
    def __init__(self):
        self.ymlfile = None
        self.testcase =None

    def all_yml_files(self,path):
        yml_list = []
        for root, dirs, files in os.walk(path):
            for _path in files:
                path = os.path.join(root, _path)
                if "yml" in path:
                    # print(path)
                    yml_list.append(path)
        return yml_list

    def class_name(self):
        class_name = os.path.split(self.ymlfile)[1][:-4]
        return class_name.capitalize()

    def file_name(self):
        file_name = os.path.split(self.ymlfile)[1][:-3]
        return file_name+"py"

    def case_name(self):
        file_name = os.path.split(self.ymlfile)[1][:-4]
        return file_name
    #case路径
    def case_path(self):
        case_path = self.ymlfile.replace("data", "testcases")
        case_dir = os.path.split(case_path)[0]
        # print(os.path.split(case_path)[0])
        # 创建文件夹
        case = pathlib.Path(case_dir)
        case.mkdir(exist_ok=True)
        return case_dir

    def epic(self):
        return  self.testcase.get("config").get("epic")
    def feature(self):
        return  self.testcase.get("config").get("feature")
    def story(self):
        return  self.testcase.get("config").get("story")

    def casegen(self):
        for yamlfile in self.all_yml_files("/Users/tim/Desktop/test_pro/pyframe/data"):
            testcase = ReadYaml(yamlfile).read_yml_file()
            print("@@@@")
            print(yamlfile)
            self.ymlfile =yamlfile
            self.testcase =testcase
            print(self.case_path())
            print(self.case_name())
            file_path = self.case_path()+"/test_"+self.file_name()
            # print(filename_path)
            print(self.file_name())
            print("@@@@")
            print(self.class_name())
            print((self.story()))
            print((self.feature()))
            print((self.epic()))
            print("!!!")

            new_python_template(filename=file_path,ymlfile=yamlfile,epic=self.epic(),feature=self.feature(),story=self.story(),
                            test_name=self.case_name(),classname=self.class_name(),pyfilename=self.file_name()

        )
if __name__ == '__main__':
    #取data目录下所有yml文件
    file =  "/Users/tim/Desktop/test_pro/pyframe/data/userinfo/deleteuserinfo.yml"
    TestCaseGener().casegen()
    # case_path = file.replace("data","testcase")
    # case_dir =os.path.split(case_path)[0]
    # print(os.path.split(case_path)[0])
    # #创建文件夹
    # case = pathlib.Path(case_dir)
    # case.mkdir()

    # print(ReadYaml("/Users/tim/Desktop/test_pro/pyframe/data/userinfo/deleteuserinfo.yml").read_yml_file())
    #os.path.split(file)[0] 文件目录
    # class_name =os.path.split(file)[1][:-4]
    # a = "test"
    # print(a.capitalize())
    # print(os.path.split(file)[1][:-3]+"py")
    # print(class_name.capitalize())
    #类名 大写
    # yml_list =[]
    # for root, dirs, files in os.walk("/Users/tim/Desktop/test_pro/pyframe/data"):
    #     # print("1", root)  # 当前正在遍历的目录路径
    #     print("*********************")
    #     # print("2", dirs)  # 当前目录下的子目录列表
    #     # print("*********************")
    #     # print("3", files)
    #     for _path in files:
    #         path = os.path.join(root, _path)
    #         if "yml" in path:
    #             # print(path)
    #             yml_list.append(path)
    #     #

