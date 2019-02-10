import numpy as np
from tkinter import *
import random
import math

from operator import itemgetter #用来对字典列表根据特定属性进行排序

MAX_DISTANCE = float('inf')
class ClosestPairs(object):

    def __init__(self, size=1000, total_w=10000, total_h=10000, canvas_w=1200, canvas_h=700):
        self.size = size

        self.window = Tk()
        self.window.title("Find Closest Pairs")

        #设定frame和canvas的显示宽高
        self.frame_w = self.canvas_w = canvas_w
        self.frame_h = self.canvas_h = canvas_h

        #创建frame
        self.frame = Frame(self.window,width=self.frame_w,height=self.frame_h)
        self.frame.grid(row=0,column=0)

        #canvas的全部宽高
        self.total_w = total_w
        self.total_h = total_h

        #创建canvas
        self.canvas = Canvas(self.frame, 
                        width=self.canvas_w, 
                        height=self.canvas_h, 
                        background="white",
                        scrollregion=(0,0,self.total_w, self.total_h)
                    )

        #canvas绑定点击事件
        self.canvas.bind("<Button -1>", self.add_point)

        #圆点半径
        self.dot_radius = 2
        #可选坐标集合
        self.x_list = list(range(self.dot_radius, self.total_w - self.dot_radius))
        self.y_list = list(range(self.dot_radius, self.total_h - self.dot_radius))
        #实际坐标集合
        # 使用random模块中的random.sample函数产生一个数值范围内的不重复的随机数
        self.posx_list = random.sample(self.x_list, size)
        self.posy_list = random.sample(self.y_list, size)

        #声明点列表
        self.points_list = []
        # self.temp_points_list = []  #存储points_list按照x和y属性排序的结果

        #水平滚动条
        self.hbar=Scrollbar(self.frame,orient=HORIZONTAL) 
        self.hbar.pack(side=BOTTOM,fill=X)
        self.hbar.config(command=self.canvas.xview) 
  
        #竖直滚动条 
        self.vbar=Scrollbar(self.frame,orient=VERTICAL)   
        self.vbar.pack(side=RIGHT,fill=Y)
        self.vbar.config(command=self.canvas.yview)

        #canvas属性设置
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set) #设置  
        self.canvas.pack(expand=True,fill=BOTH)

    def generate_random_points(self):    
        for i in range(self.size):
            point = {}
            point["x"] =  self.posx_list[i]
            point["y"] =  self.posy_list[i]
            self.points_list.append(point)
            self.canvas.create_oval(self.posx_list[i]-self.dot_radius, self.posy_list[i]-self.dot_radius, self.posx_list[i]+self.dot_radius, self.posy_list[i]+self.dot_radius, fill='red')
        self.window.mainloop()

    def sort_x(self, points_list):
        return sorted(points_list, key=itemgetter('x'))
        

    def sort_y(self, points_list):
        return sorted(points_list, key=itemgetter('y'))

    
    def get_distance(self, point_a, point_b):
        return math.sqrt((point_a["x"]-point_b["x"])**2 + (point_a["y"]-point_b["y"])**2)

    def get_closest_pairs(self, left, right):
        if left == right:
            return MAX_DISTANCE
        if left+1 == right:
            return self.get_distance(self.points_list[left], self.points_list[right])

        mid = (left + right) // 2    #取x的中点
        d1 = self.get_closest_pairs(left, mid)
        d2 = self.get_closest_pairs(mid, right)
        d = min(d1, d2)

        temp_list = []
        for i in range(left, right+1):
            if math.fabs(self.points_list[i]["x"] - self.points_list[mid]["x"]) <= d:
                temp_list.append(self.points_list[i])

        temp_list = self.sort_y(temp_list)
        temp_len = len(temp_list)
        for i in range(temp_len):
            for j in range(i+1, temp_len):
                #不超过六个点进入此循环
                if temp_list[j]['y'] - temp_list[i]['y'] < d:
                    d3 = self.get_distance(temp_list[i], temp_list[j])
                    d = min(d, d3)
                else:
                    break
        return d
    
    def add_point(self,event):
        self.canvas.create_oval(event.x-self.dot_radius, event.y-self.dot_radius,event.x+self.dot_radius, event.y+self.dot_radius, fill='blue')
        # self.window.mainloop()
        pass
        

if __name__ == '__main__':
    closest_pairs = ClosestPairs(1000,2000,2000)
    closest_pairs.generate_random_points()
    closest_pairs.points_list = closest_pairs.sort_x(closest_pairs.points_list)
    print(closest_pairs.get_closest_pairs(0, 999))