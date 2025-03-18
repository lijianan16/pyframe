#[{"code":"$.code","check":"eq"},{"city":"$.data.city","check":"eq"}]
#check key值默认是selfdata里函数名
#$.data.city是一个实际值，通过eq这个方法 预期值比较
#字符串，怎么去访问函数（eq)
#返回object对象的属性和属性值字典对象
from common.base import pro_path
from common.selfassert.selfassert import SelfAssert
from common.utils.filterdata import json_path


#字典
# print(vars(SelfAssert))
# print(vars(SelfAssert).items())

def compare():
    dic={}
    for key ,value in vars(SelfAssert).items():
        dic[key] =value
    return dic

# c  = compare()
# print(type(c))
# fun = c["lt"]
# print(type(fun))
# fun(2,2)

def verifyres(response,expect,expr):
    #结果列表+字典 [{"code":None,"status":1},{"city":None,"status":0}] 0,false;1,true,只要有一个0则为false
    result =[]
    for dic_jpath in expr:
        check= dic_jpath["check"]
        #遍历字典
        #{"code":"$.code","check":"eq"}
        for key in dic_jpath.keys():
            if key != "check":
                actual_value = json_path(response,dic_jpath[key])
                try:
                    ex = expect[key]
                    #调用比较方法
                    func = compare()[check]
                    func(actual_value[0],ex)
                    status = 1

                except(AssertionError,TypeError,KeyError) as e:
                    print(e)
                    status = 0
                finally:
                    #一直执行
                    result.append({key:actual_value,"status":status})
    print(result)
    return  result

#[{'code': ['200'], 'status': 1}, {'city': False, 'status': 0}]
#最终状态0,1
def result_status(result):
    #result不为空
    for res in result:
        if res["status"] == 0:
            status = 0
            break
        else:
            status = 1
    return status


if __name__ == '__main__':
    # actual  = [{"code":"$.code","check":"eq"},{"city":"$.city","check":"eq"}]
    # ac = [{"purpose": "$.purpose", "check": "eq"}]
    # expect =  {"code":"200","city":"上海"}
    # #断言
    # #函数有问题
    # res = verifyres(expect,expect,ac)
    # print(result_status(res))
    my_log_file_path = pro_path() + "logs/"
    print(my_log_file_path)