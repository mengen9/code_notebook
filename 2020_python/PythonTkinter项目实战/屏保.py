'''
屏保项目分析
世界构成
球
    1大小随机
    2颜色随机
    3速度随机
    4初始位置随机
    5创建球的函数
    6创建移动球的函数
屏保类
    操作球即可
'''
import random
from tkinter import *
from tkinter import messagebox
class RandomBall():
    def __init__(self, canvas, screenwidth, screenheight):
        self.canvas = canvas
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.x = random.randint(60, int(screenwidth - 60))
        self.y = random.randint(60, int(screenheight - 60))
        self.xvolecity = random.randint(6, 12)
        self.yvolecity = random.randint(6, 12)
        self.radius = random.randint(40, 70)
        c = lambda:random.randint(0, 255)
        self.color = "#%02x%02x%02x" % (c(), c(), c())
    def create_ball(self):
        x1 = self.x - self.radius
        y1 = self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.y + self.radius

        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 球的移动速度
        self.x += self.xvolecity
        self.y += self.yvolecity

        if self.x + self.radius >= self.screenwidth:
            self.xvolecity = -self.xvolecity
        if self.x - self.radius <= 0:
            self.xvolecity = -self.xvolecity
        if self.y + self.radius >= self.screenheight:
            self.yvolecity = -self.yvolecity
        if self.y - self.radius <= 0:
            self.yvolecity = -self.yvolecity
        self.canvas.move(self.item, self.xvolecity, self.yvolecity)


class ScreenSaver():
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.root.bind("<Motion>", self.et)
        self.root.bind("<Any-Button>", self.info)
        self.root.bind("<Key>", self.et)
        self.balls = []
        self.num_ball = random.randint(8, 20)
        for i in range(self.num_ball):
            ball = RandomBall(self.canvas, self.width, self.height)
            ball.create_ball()
            self.balls.append(ball)
        self.screen_saver_run()
        self.root.mainloop()
    def screen_saver_run(self):
        for i in self.balls:
            i.move_ball()
        self.canvas.after(50, self.screen_saver_run)
    def et(self, e):
        self.root.destroy()
    def info(self, e):
        messagebox.showinfo("ScreenSaver", "曾经小小少年\n如今风度翩翩")

if __name__ == '__main__':
    ScreenSaver()