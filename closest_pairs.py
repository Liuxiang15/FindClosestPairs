# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author:洪卫
 
# import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上设定标签
# var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# l.pack()
 
# # 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')
 
# # 第5步，在窗口界面设置放置Button按键
# b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
# b.pack()
 
# # 第6步，主窗口循环显示
# window.mainloop()

# import numpy as np
# import matplotlib.pyplot as plt
# N = 1000
# x = np.random.randn(N)
# y = np.random.randn(N)
# color = ['r','y','k','g','m']
# plt.scatter(x, y)
# plt.show()

# from tkinter import *
#     canvas=Canvas(width=300,height=300,bg='green')
#     canvas.pack(expand=YES,fill=BOTH)
#     x0=150    #圆心横坐标
#     y0=100    #圆心纵坐标
#     canvas.create_oval(x0-10,y0-10,x0+10,y0+10)    #圆外矩形左上角与右下角坐标
#     canvas.create_oval(x0-20,y0-20,x0+20,y0+20)    #圆外矩形左上角与右下角坐标
#     canvas.create_oval(x0-50,y0-50,x0+50,y0+50)    #圆外矩形左上角与右下角坐标

import numpy as np
from tkinter import *

class ClosestPairs(object):

    # def __init__(self,canvas_w, canvas_h, num=1000):
    #     self.

    pass

root=Tk()
root.title("Find Closest Pairs")

frame_w = 1000
frame_h = 700
frame = Frame(root,width=frame_w,height=frame_h)
frame.grid(row=0,column=0)

canvas_w = 1000
canvas_h = 700

canvas = Canvas(
	frame,
	width=canvas_w,
	height=canvas_h,
	background="white",
    scrollregion=(0,0,10000, 10000)
	)

# canvas.pack()

dot_width = 4

hbar=Scrollbar(frame,orient=HORIZONTAL)#水平滚动条 
# hbar.place(x =0,y=400,width=5000,height=10) 
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview) 

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set) #设置  

canvas.pack(expand=True,fill=BOTH)



def generate_random_points(num,canvas):
    #随机生成num个圆点(其实是用颜色填充的圆)
    posx_list = np.random.random_integers(0,canvas_w-4,size=num).tolist()
    posy_list = np.random.random_integers(0,canvas_w-4,size=num).tolist()
    for i in range(num):
            canvas.create_oval(posx_list[i], posy_list[i], posx_list[i]+dot_width, posy_list[i]+dot_width, fill='red')


generate_random_points(1000,canvas)

mainloop()


# from tkinter import *
# root=Tk()

# frame=Frame(root,width=300,height=300)
# frame.grid(row=0,column=0)

# canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

# hbar=Scrollbar(frame,orient=HORIZONTAL)
# hbar.pack(side=BOTTOM,fill=X)
# hbar.config(command=canvas.xview)

# vbar=Scrollbar(frame,orient=VERTICAL)
# vbar.pack(side=RIGHT,fill=Y)
# vbar.config(command=canvas.yview)

# canvas.config(width=300,height=300)
# canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# canvas.pack(side=LEFT,expand=True,fill=BOTH)

# root.mainloop()