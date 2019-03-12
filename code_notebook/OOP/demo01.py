'''
定义一个学生类，来描述一个学生的基本信息
'''
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





