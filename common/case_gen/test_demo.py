# 创建并写入Python模板文件
def create_python_template(filename, classname):
    # 打开文件用于写入
    with open(filename, 'w') as file:
        # 写入模板内容
        file.write("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""")
        # 添加函数模板
        file.write(f"""
def test_{classname}():
    # 在这里写下函数的主体
    print("大牛测试欢迎你")


""")


# 调用函数创建模板文件
create_python_template('template.py', classname="Test2")