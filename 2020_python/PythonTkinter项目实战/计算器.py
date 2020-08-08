"""
计算器项目
布局使用Place,利用容器来装相应的组件，具有菜单项顶级菜单
相关函数
数字的操作函数
字符的操作函数
相关运算的操作函数
"""
from tkinter import *
from tkinter import messagebox
import operator


class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("小破孩蘑菇头计算器")
        self.master.geometry("300x315+500+200")
        self.master.resizable(0, 0) # 边框不允许调整
        self.rst1 = StringVar() # 计算器过程显示对象
        self.rst1.set("0")
        self.rst2 = StringVar() # 计算器结果显示框对象
        self.rst2.set("")
        self.lists = []
        self.menu_tools()
        self.master.bind("<KeyPress-F1>", self.show_info)
        self.create_widget()
        self.mainloop()

    def create_widget(self):
        # 先创建计算过程和结算结果的容器
        label_frame = Frame(self.master, width=300, height=60, bg="pink")
        label_frame.place(x=0, y=0)
        label02 = Label(label_frame, textvariable=self.rst2, width=300, height=30, bg="orange",font=("黑体",15,"bold"), justify=LEFT, anchor="e")
        label02.place(relx=0,rely=0,width=300,height=30)
        label01 = Label(label_frame,textvariable=self.rst1, width=300, height=30, bg="pink", font=("黑体",20,"bold"), justify=LEFT, anchor="e")
        label01.place(relx=0, rely=0.5, width=300, height=30)
        button_frame = Frame(self.master, width=300, height=340, bg="#0ceecc")
        button_frame.place(x=0, y=60)
        btn_AC = Button(button_frame, text="AC",command=self.clear)
        btn_AC.place(x=10,y=10,width=60, height=40)
        btn_Sqrt = Button(button_frame, text="Sqrt", command=self.sqrt)
        btn_Sqrt.place(x=85, y=10, width=60, height=40)
        btn_Power = Button(button_frame, text="Power", command=self.power)
        btn_Power.place(x=155, y=10, width=60, height=40)
        btn_back = Button(button_frame, text="←",command=self.rollback)
        btn_back.place(x=225,y=10,width=60,height=40)
        num_btn = Button(button_frame, text="7", command=lambda:self.press_num("7"))
        num_btn.place(x=10, y=60, width=60, height=40)
        num_btn = Button(button_frame, text="8", command=lambda:self.press_num("8"))
        num_btn.place(x=85, y=60, width=60, height=40)
        num_btn = Button(button_frame, text="9", command=lambda:self.press_num("9"))
        num_btn.place(x=155, y=60, width=60, height=40)
        num_btn = Button(button_frame, text="÷", command=lambda:self.operation("/"))
        num_btn.place(x=225, y=60, width=60, height=40)
        num_btn = Button(button_frame, text="4", command=lambda:self.press_num("4"))
        num_btn.place(x=10, y=110, width=60, height=40)
        num_btn = Button(button_frame, text="5", command=lambda:self.press_num("5"))
        num_btn.place(x=85, y=110, width=60, height=40)
        num_btn = Button(button_frame, text="6", command=lambda:self.press_num("6"))
        num_btn.place(x=155, y=110, width=60, height=40)
        num_btn = Button(button_frame, text="x", command=lambda:self.operation("*"))
        num_btn.place(x=225, y=110, width=60, height=40)
        num_btn = Button(button_frame, text="1", command=lambda:self.press_num("1"))
        num_btn.place(x=10, y=160, width=60, height=40)
        num_btn = Button(button_frame, text="2", command=lambda:self.press_num("2"))
        num_btn.place(x=85, y=160, width=60, height=40)
        num_btn = Button(button_frame, text="3", command=lambda:self.press_num("3"))
        num_btn.place(x=155, y=160, width=60, height=40)
        num_btn = Button(button_frame, text="-", command=lambda:self.operation("-"))
        num_btn.place(x=225, y=160, width=60, height=40)
        num_btn = Button(button_frame, text="0", command=lambda:self.press_num("0"))
        num_btn.place(x=10, y=210, width=60, height=40)
        num_btn = Button(button_frame, text=".", command=lambda:self.press_num("."))
        num_btn.place(x=85, y=210, width=60, height=40)
        num_btn = Button(button_frame, text="=", command=lambda:self.cal_result("="))
        num_btn.place(x=155, y=210, width=60, height=40)
        num_btn = Button(button_frame, text="+", command=lambda:self.operation("+"))
        num_btn.place(x=225, y=210, width=60, height=40)

    def clear(self):
        self.lists.clear()
        self.rst1.set("0")
        self.rst2.set("")

    def sqrt(self):
        if len(self.lists) != 0:
            if self.lists[-1] in ["+", "-", "*", "/"]:
                del self.lists[-1]
            else:
                com_str = "".join(self.lists)
                end_rst = eval(com_str)
                end_rst = end_rst ** 0.5
                self.rst1.set("√(" + com_str + ")")
                self.rst2.set(end_rst)
                self.lists.clear()
                self.lists.append(str(end_rst))

    def power(self):
        if len(self.lists) == 0:
            self.rst2.set("0的平方还是0")
            self.rst1.set("0")
        else:
            if self.lists[-1] in ["+", "-", "*", "/"]:
                del self.lists[-1]
            else:
                new_str = "".join(self.lists)
                end_num = eval(new_str)
                end_num = end_num * end_num
                self.rst2.set(end_num)
                self.rst1.set("(" + new_str + ")^2")
                self.lists.clear()
                self.lists.append(str(end_num)) # 这里必须转换成字符型才能拼接相加，数据类型不同的不允许拼接

    def operation(self, op):
        if len(self.lists) > 0:
            if self.lists[-1] in ["+", "-", "*", "/"]:
                self.lists[-1] = op # 以上代码表示可以随时更换加减乘除
            else:
                self.lists.append(op)
            self.rst1.set("".join(self.lists))
        else:
            self.rst2.set("没有可加的对象！")

    def cal_result(self, op1):
        if op1 == "=":
            if len(self.lists) > 0:
                if operator.eq(self.lists, ['1','+']):
                    self.lists.clear()
                    self.rst2.set("机会来了，猪都可以上天！")
                    self.rst1.set("0")
                else:
                    if self.lists[-1] in ["+", "-", "x", "/"]:
                        del self.lists[-1]
                    else:
                        new_str = "".join(self.lists) # 这里转换成字符串是为了后面的过程框接收字符串用的
                        end_rst = eval(new_str)
                        self.rst2.set(end_rst)
                        self.rst1.set(new_str)
                        self.lists.clear()
                        self.lists.append(str(end_rst)) # 供下次继续计算，这里必须要做一个转换，将数值型转换成字符串

    def press_num(self, num):
        self.lists.append(num)
        self.rst1.set("".join(self.lists))

    def rollback(self):
        if len(self.lists) > 0:
            del self.lists[-1]
            if len(self.lists) == 0:
                self.rst1.set("0")
            else:
                com_str = "".join(self.lists)
                self.rst1.set(com_str)
        else:
            self.rst2.set("没有要删除的对象")

    def menu_tools(self):
        menubar = Menu(self.master)
        aboutmenu = Menu(menubar, tearoff=0)
        moremenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="关于", command=self.about)
        moremenu.add_command(label="更多", command=self.more)
        menubar.add_cascade(label="Creator", menu=aboutmenu)
        menubar.add_cascade(label="帮助", menu=moremenu)
        self.master.config(menu=menubar)
    def about(self):
        messagebox.showinfo("Message", "Desinger by mengen")

    def more(self):
        messagebox.showinfo("Help", "还没有写好帮助文档，有时间在写")

    def show_info(self, e):
        messagebox.showinfo("快捷键窗口", "人生弯弯曲曲水\n岁岁重重叠叠山")


if __name__ == '__main__':
    root = Tk()
    Calculator(root)