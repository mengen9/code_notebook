"""
函数复习
"""
"""
编写函数指南
    编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字符和下划线。描述性名称可帮助你和别人明白
代码想要做什么。给模块命名时也应遵循上述约定。
    每个函数都应该含简要的阐述其功能注释，该注释应紧跟在函数定义后面，并采用文档字符格式，文档良好的函数让其他程序员只
需阅读文档字符串中的描述就能够使用它，他们全完可以相信代码如描述的那样运行，只要知道函数名称、需要的实参以及返回值的类型
就能够在自己的程序中使用它。

给形参指定默认值时，等号两边不要有空格：
    def function_name(parameter_0, parameter_1='default value')
对于函数调用中的关键字实参，也应该遵循这种约定
    function_name(value_0, parameter_1='value')
PEP8(https://www.python.org/dev/peps/pep-0008/)
"""
# 在函数中修改列表
# 禁止函数修改列表
    # 可以利用切边实现：创建一个unprint_modles副本，利用切片实现
def print_modles(unprint_modles, completed_prints):
    while unprint_modles:
        current_modles = unprint_modles.pop()
        print("\nprinting modle : {}".format(current_modles))
        completed_prints.append(current_modles)
def show_completed_modles(comleted_prints):
    print("The follwing models have been printed")
    for i in comleted_prints:
        print(i)
unprint_modles = ["3D实体设计", "Soldworks", "NX"]
completed_prints = []
print_modles(unprint_modles,completed_prints)
show_completed_modles(completed_prints)
# 函数：传递任意数量的实参-收集参数
def caxa_plm_modules(*args):
    print(type(args))
    for i in args:
        print(i, end=" ")

caxa_plm_modules("图文档", "红线批注", "电子签名", "工作流")
# 结合使用位置实参和任意数量实参
    # 位置参数和关键字参数的小练习
    # 注意：此时的位置参数(普通参数)必须放在收集参数前面
def plm_modules(licenses, *args):
    print("\n欣达集团licenses:{}".format(licenses))
    for i in args:
        print(i, end=" ")
    print()


plm_modules(70, "图文档", "红线批注", "电子签名", "工作流")

# 使用任意数量的关键字参数
def build_profile(first_name, last_name, **kwargs):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for k, v in kwargs.items():
        profile[k] = v
    return profile

rst = build_profile('meng', 'en', location='Ningbo', field='PLM实施工程师')
print(rst)

"""
将函数存储在模块中
"""