import abc
class A:
    name = "jupyter"
    age = 18


print(A.__dict__)   # A为类实例


a = A()     # 创建个对象，类的实例化
print(a.age)    # 访问类中的属性
print(a.__dict__)
print(a.name)
class B:
    name = "mengen"
    age = 23
    def say(self):
        self.name = "aaaa"
        self.age = 19
        print("My name is {0},and age is {1}".format(self.name, self.age))
# 此案例说明
# 类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量


print(B.name)
print(B.age)
print("*"*50)
print(id(B.name))
print(id(B.age))
print("%"*20)
a = B()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
a.say()
print(B.__dict__)
print(a.__dict__)
class Teacher:
    name = "megnen"
    age = 23
    def say(self):
        self.name = "xiaoen"
        self.age = 17
        print("My name is {},and {} years old".format(self.name, __class__.age))    # 非绑定类方法中也可以使用类的成员
    @staticmethod
    def sayagain():     # 绑定类，必须通过类来访问
        print("Hello,nice to see you again")
        print(__class__.name)
        print(__class__.age)


t = Teacher()
t.say()
print("下面是绑定类的函数访问方法")
Teacher.sayagain()
class C:
    name = "mengen9"
    age = 20
    def __init__(self):
        self.name = "xiao hapi"
        self.age = 25
    def say(self):
        print(self.name)
        print(self.age)
class D:
    name = "dfssf"
    age = 90


c = C()
c.say()
C.say(C)  # 非绑定类函数必须有一个参数，此参数可以是对象实例也可以是类名
C.say(D)  # Python中经典的鸭子模型'''

"""
私有变量案例
"""


class Person:
    name = "xiaopohai"
    __age = 20


p = Person
print(p.name)
# print(p.__age)
# name mangling技术
p._Person__age = 20  # 强制访问
print(p._Person__age)
# 继承的语法
class Person:
    name = "No name"
    age = 18
    _score = 0  # 受保护的属性
    __petname = "sec"   # 私有变量
    @staticmethod
    def sleep():    # 绑定类方法
        print("sleepping...........")

    @staticmethod
    def work():
        print("make some money")


class Teacher(Person):  # 继承父类
    name = "dana"
    @staticmethod
    def make_test():
        print("给学生考试")
    def work(self):     # 扩充父类相应的功能
        Person.work()
        # super().work()# 调用父类的另一种方法
        print("改作业")
        self.make_test()


t = Teacher()
print(t.name)
print(Teacher.name)
#   print(t.__petname)  # 访问私有的属性报错
t.sleep()   # 对象可以访问类的方法和成员
t.work()
# 构造函数的概念
class Dog:
    def __init__(self):     # __init__就是构造函数，没吃实例化的时候，第一个被调用，因为主要工作就是进行初始化，所以得名
        print("I am init in Dog")


#   kaka = Dog()
#   继承中的构造函数
class Animal:
    def __init__(self):
        print("I am __init__ Animal")
class PaXingAni(Animal):
    def __init__(self, name):     # 这里的构造函数，由于狗类中的构造函数已经定义啦，则不在调用父类的构造函数
        print("paxingdongwu")
        print("PaXing Dongwu {}".format(name))
class Dog(PaXingAni):
    """
     调用父类构造函数的第一种方式
        def __init__(self, name):     # __init__就是构造函数，没有实例化的时候，第一个被调用，因为主要工作就是进行初始化，所以得名
            PaXingAni.__init__(self, name)  # 首先调用父类的构造函数
            print("我是附加的构造函数")  # 其次调用自己的构造函数，在增加自己的功能
            print("I am init in Dog")
            print("我结束啦")
    """
#   调用父类构造函数的第二种方式
    def __init__(self, name):
        super(Dog, self).__init__(name)  # 首先调用父类的构造函数
        print("我是附加的构造函数")  # 其次调用自己的构造函数，在增加自己的功能
        print("I am init in Dog")
        print("我结束啦")
class Cat(PaXingAni):
    pass


kaka = Dog("dd")
c = Cat("xiaoxiao")     # 此时，由于Cat没有构造函数，则向上查找，因为PaXingAni的构造函数需要两个参数，实例化的时候就给了一个报错
"""
    print(type(super))
    help(super)
"""
class A:
    pass
class B(A):
    pass


print(A.__mro__)
print(B.__mro__)    # 查找B的所有父类

"""
多继承的案例
"""
class Fish:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def swim():
        print("I am swimming..........")
class Brid:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def fly():
        print("i am flying.......")
class Person:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def work():
        print("working..........")
class SuperMan(Fish, Brid, Person):     # 多继承案例
    def __init__(self, name):
        self.name = name
class Student(Person):  # 单继承的案例
    def __init__(self, name):
        self.name = name


s = SuperMan("xiaoxaio")
s.work()
s.fly()
s.swim()
stu = Student("yaya")
stu.work()


class A:
    pass


a = A()
print(dir(A))

class Stu:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print_score(self):
        print("my name is {} and {} year old".format(self.__name, self.__age))


s = Stu("xaiohapi", 2)
s.print_score()
# print(s.__name)     # 私有的属性，在外部无法访问
# 这里也可以访问私有的变量，实际是一种python mangling技术
# __name 等同于 _Stu__name
s._Stu__name = "zhuxiaopi"  # name mangling技术
print(s._Stu__name)

# 多态的案例
class Animal:
    def run(self):
        print("Animal is running..........")
class Dog(Animal):
    def run(self):
        print("Dog is running..............")
class Cat(Animal):
    def run(self):
        print("Cat is running..............")
class Tortoise(Animal):
    def run(self):
        print("Tortoise is slowly...........")
def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()
t = Tortoise()
print("a is Animal", isinstance(a, Animal))     # 判断是否为父子类关系
print("a is Dog", isinstance(a, Dog))
print("a is Cat", isinstance(a, Cat))
print("d is Animal", isinstance(d, Animal))
print("d is Dog", isinstance(d, Dog))
print("d is Cat", isinstance(d, Cat))
run_twice(d)    # 多态的调用方式
run_twice(c)
run_twice(t)


class Student:
    def __init__(self):
        self._score = None
    def get_score(self):
        #   return self._score
        print(self._score)
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100")
        self._score = value


s = Student()
s.set_score(100)
s.get_score()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setname(name)
    def setname(self, name):
        self.name = name.upper()
    def intro(self):
        print("my name is {}, and {} years old".format(self.name, self.age))


p1 = Person("XIAO Guang", 20)
p2 = Person("Da guang", 18)
p1.intro()
p2.intro()
# 代码改进:property案例
# 定义个Person类，具有name,age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一用整数的格式
# f = property(fget, fset, fdel, doc)
class Personal:
    """
    这是一个人类，一个高尚的人，一个脱离低级趣味的人
    """
    def __init__(self):
        self._name = "NoName"
        self._age = 0
    def fget(self):     # 读操作
        return self._name * 2
    def fset(self, name):   # 写操作
        self._name = name.upper()
    def fdel(self):     # 删除操作
        self._name = "NoName"
    name = property(fget, fset, fdel, "对name属性进行操作")    # 注意property四个参数的顺序
    @property
    def print_age(self):
        return self._age * 2
    @print_age.setter
    def print_age(self, value):
        if not isinstance(value, int):
            raise ValueError("age must be an integer")
        if value < 0 or value > 200:
            raise ValueError("age is between 0~200")
        self._age = value


p3 = Personal()
p3.name = "xiaohaPi"
print(p3.name)
p4 = Personal()
p4.print_age = 200
print('您的年龄是', p4.print_age)
print(Personal.__dict__)
print(Personal.__doc__)
print(Personal.__name__)
print(Personal.__bases__)
# __call__函数的举例
class A:
    def __init__(self):
        print("我是构造函数，我被调用啦")
    def __call__(self):    # 对象当函数使用时，会触发此函数
        print("我又被调用啦一次")
    def __str__(self):  # 当对象被当做字符串使用时会自动调用改函数
        return "这是魔法函数的例子"


a = A()
a()
print(a)
# __getattr__案例；访问一个不存在的属性是触发
class B:
    name = "NoName"
    age = 18
    def __getattr__(self, name):
        print("没找到啊没找到")
        # return name


b = B()
print(b.name)
print(b.age)
print(b.gender)
"""
__setattr__案例
对成员属性进行设置的时候触发
该方法不能直接对属性进行赋值操作，否则会导致死循环
"""
class Person:
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性：{}".format(name))
        # 下面语句会导致死循环:该方法不能直接对属性进行赋值操作
        # self.name = value
        super(Person, self).__setattr__(name, value)


p = Person()
print(p.__dict__)
p.age = 18
"""
__gt__案例
    - __gt__:进行大于判断的时候触发的函数
    - 参数
        - self
        - 第二个参数是第二个对象
        - 返回值可以是任意值，推荐返回布尔值
        - 案例参考Student
"""
class Student:
    def __init__(self, name):
        self.name = name
    def __gt__(self, obj):
        print("哈哈吗{0}会比{1}大吗？".format(self, obj))
        return self._name > obj._name


stu1 = "python"
stu2 = "java"
print(stu1 > stu2)

"""
三种类方法的案例
"""
class Person:
    def eat(self):
        print(self)
        print("Eating......")
    # 类方法：类方法的第一个参数，一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.....")
    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying..........")


yueyue = Person()
yueyue.eat()
yueyue.play()
yueyue.say()
"""
抽象类的实现案例
"""
class Human(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def smoking(self):
        pass
    @abc.abstractclassmethod
    def drink(cls):
        pass
    @abc.abstractstaticmethod
    def play():
        pass
class Chinese(Human):
    def smoking(self):
        print("很少抽雪茄")
    def drink(self):
        print("很少喝红酒")
    def play(self):
        print("打豆豆")


c = Chinese()
c.smoking()
c.play()
c.drink()

"""
函数名当变量来用的案例
"""
def sayhello(name):
    print("{0}你好，来一发吗".format(name))


sayhello("小蝴蝶")
liumang = sayhello
liumang("xiaohudie")


"""
自定义类的例子
"""
def say(self):
    print("saying...........")
def talk(self):
    print("talking................")


A = type("Aclassname", (object,), {"class_say": say, "class_talk": talk})
a = A()
print(dir(a))
a.class_say()
a.class_talk()
"""
元类的演示
"""
class YuanLeiMetaCalss(type):
    def __new__(cls, name, bases, attrs):
        print("this is a metaclass")
        attrs['id'] = 'CAXA001'
        attrs['addr'] = "杭州市拱墅区祥园路6号"
        return type.__new__(cls, name, bases, attrs)    # 自己的业务处理
# 元类定义完就可以使用，使用注意写法
class Teacher(object, metaclass=YuanLeiMetaCalss):
    pass


t = Teacher()
# print(t.__dict__)
print(t.id)
print(t.addr)




















