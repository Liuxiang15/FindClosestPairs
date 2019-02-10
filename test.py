'''3.使用回调函数（不建议这样使用）'''
# -*- coding: utf-8 -*-
from tkinter import *
 
root = Tk()
 
 
def scrollCall(moveto, pos,x):
    # 如何得到两个参数：使用如下打印中的信息，可以看到解释器传给scrollCall函数的两个参数，一个为
    # moveto,参考手册可以得知，它是当拖动slider时调用的函数；另一个参数为slider的当前位置，我们
    # 可以通过set函数来设置slider的位置，因此使用这个pos就可以完成控制slider的位置。
    # print moveto,pos
    # sl.set(pos, 0)
    # print(sl.get())
    print("进入scrollCall")
    print(moveto)
    print(pos)
    print(x)
 
 
sl = Scrollbar(root, orient=HORIZONTAL, command=scrollCall)
sl.pack()
root.mainloop()
# 这样还有一个严重问题，只能对其进行拖动。对两个按钮及pagedwon/pageup的响应，由于up按钮响应的为三个参数，故会出
# 现异常。这个例子只是用来说明command属性是可用的，如果喜欢自己可以处理所有的消息，将scrollCall是否可以改为变参数函数？
# 对于不同的输入分别进行不同的处理。