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