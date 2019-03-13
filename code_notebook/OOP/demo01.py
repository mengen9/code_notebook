import math
'''import函数中调用方法和Java中类似，直接对象.方法或者是类.方法，注意函数返回的结果为浮点型
#像上取整
print(math.ceil(5.001))
print(math.floor((5.07)))
#打印系统关键字
import keyword
print(keyword.kwlist)'''
'''l = [i for i in range(5)]
 print(l)'''
'''递归
def recursion(n):
    print(n)
    if n>0:
        recursion(n-1)
    else:
        print("弹栈")
    print(n)
recursion(4)
print(math.sqrt(3))
print(int(math.pow(2,3)))#类型的强制转换
print(math.fabs(-5))
print(abs(-4))#返回值得数据类型由本身值决定
print(abs(-5.6))
#元组拆分函数
print(math.modf(8.3))
import random
for i in range(10):
    # print(random.random())
    print(random.randint(1,8))
'''
#定义一个学生类，来描述一个学生的基本信息
#定义一个学生空类
class Student():
    pass
#定义(生成一个对象)
pupyter = Student()
class PythonStu():
    #用None给对象赋值
    name = None
    age = 18
    lover = "Python"
    #注意
    #1.def doHomework的缩进层级
    #2.self是系统默认参数
    def doHomework(self):
        print("我在做作业")
        return None
#实例化一个jupyter对象
jupyter = PythonStu()
print(jupyter.age)
print(jupyter.lover)
print(jupyter.name)
jupyter.doHomework()
#字母C是切换到编辑界面
#esc是退出编辑界面
print("键盘c是编辑界面啊")






