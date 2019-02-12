# coding=utf-8
"""
Created on 2019.2.10
@author: 刘祥
分治求最短点对算法参考博客：https://blog.csdn.net/Lytning/article/details/25370169
"""
import numpy as np
from tkinter import *
import random
import math

from operator import itemgetter #用来对字典列表根据特定属性进行排序

import time
import copy

MAX_DISTANCE = float('inf')
class ClosestPairs(object):

    def __init__(self, size=1000, total_w=10000, total_h=10000, canvas_w=1200, canvas_h=700):
        self.size = size

        self.window = Tk()
        self.window.title("Find Closest Pairs")

        #设定frame和canvas的显示宽高
        self.frame_w = self.canvas_w = canvas_w
        self.frame_h = self.canvas_h = canvas_h

        #创建包含canvas的frame
        self.frame = Frame(self.window,width=self.frame_w,height=self.frame_h)
        self.frame.pack(side=BOTTOM)
        # self.frame.grid(row=0,column=0)

        #创建输出调试信息和运行时间比较的frame
        # self.info_frame_h = 20
        # self.info_frame = Frame(self.window,width=self.frame_w, height=self.info_frame_h)
        # self.frame.pack(side=TOP)


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
        # self.x_list = list(range(self.dot_radius, self.total_w - self.dot_radius))
        # self.y_list = list(range(self.dot_radius, self.total_h - self.dot_radius))
        # #实际坐标集合
        # # 使用random模块中的random.sample函数产生一个数值范围内的不重复的随机数
        # self.posx_list = random.sample(self.x_list, size)
        # self.posy_list = random.sample(self.y_list, size)

        self.posx_list = []
        self.posy_list = []


        #声明点列表
        self.points_list = []
        # self.temp_points_list = []  #存储points_list按照x和y属性排序的结果

        #水平滚动条
        self.hbar=Scrollbar(self.frame,orient=HORIZONTAL) 
        self.hbar.pack(side=BOTTOM,fill=X)
        self.hbar.config(command=self.xview) 
        self.hbar_offset = 0
  
        #竖直滚动条 
        self.vbar=Scrollbar(self.frame,orient=VERTICAL)   
        self.vbar.pack(side=RIGHT,fill=Y)
        self.vbar.config(command=self.yview)
        self.vbar_offset = 0

        #canvas属性设置
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set) #设置  
        self.canvas.pack(expand=True,fill=BOTH)

        #存储最近的两个点
        self.point_a = {}
        self.point_b = {}

        #为了寻找最近点对，存储当前的距离
        self.curr_distance = MAX_DISTANCE

        #在界面上输出信息
        self.info_text = Text(self.window, width=self.frame_w, height=20) #这里设置文本框高，可以容纳5行
        self.info_text.pack(side=TOP)

        #创建关闭界面按钮
        # self.btn = Button(self.canvas, text="close window", command=self.close_window)
        # self.btn.pack(side=LEFT)


    def xview(self, MOVETO, f):
        self.canvas.xview(MOVETO,f)
        # print(MOVETO)
        self.hbar_offset = round(float(self.total_w*eval(f)))
        # print("移动百分比",eval(f))
        # print("移动的像素是%f\n"%float(self.total_w*eval(f)))

    def yview(self, MOVETO, f):
        self.canvas.yview(MOVETO,f)
        # print(MOVETO)
        self.vbar_offset = round(float(self.total_w*eval(f)))
        # print("移动百分比",eval(f))
        # print("移动的像素是%f\n"%float(self.total_w*eval(f)))

    def generate_random_points(self): 
        #创建随机点函数会包括重复点
        self.posx_list = np.random.random_integers(self.dot_radius, self.total_w - self.dot_radius, size=self.size)
        self.posy_list = np.random.random_integers(self.dot_radius, self.total_w - self.dot_radius, size=self.size)
        for i in range(self.size):
            point = {}
            point["x"] =  self.posx_list[i]
            point["y"] =  self.posy_list[i]
            self.points_list.append(point)   
            self.canvas.create_oval(self.posx_list[i]-self.dot_radius, self.posy_list[i]-self.dot_radius, self.posx_list[i]+self.dot_radius, self.posy_list[i]+self.dot_radius, fill='red')
        # self.window.mainloop()

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
            dis = self.get_distance(self.points_list[left], self.points_list[right])
            #加入寻找最近点对的相关代码
            if dis < self.curr_distance:
                self.curr_distance = dis
                self.point_a = self.points_list[left]
                self.point_b = self.points_list[right]
            return dis

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
                    #加入寻找最近点对的相关代码
                    if d == d3 and d < self.curr_distance:
                        self.curr_distance = d
                        self.point_a = temp_list[i]
                        self.point_b = temp_list[j]
                else:
                    break
        return d
    
    def add_point(self, event):
        new_point = {}
        new_point["x"] = self.hbar_offset + event.x
        new_point["y"] = self.vbar_offset + event.y
        print_str = "点击的坐标是(%4d,%4d)"%(new_point["x"],new_point['y'])
        # print(print_str)
        self.insert_info(print_str)
        #判断点是否重复
        if new_point in self.points_list:
            print_str = "您点击的点已经记录在界面上存在！" 
            # print(print_str)
            self.insert_info(print_str+"\n")
            return
        self.size += 1
        self.canvas.create_oval(new_point["x"]-self.dot_radius,new_point["y"]-self.dot_radius,new_point["x"]+self.dot_radius, new_point["y"]+self.dot_radius, fill='blue')
        self.points_list.append(new_point)
        self.points_list = self.sort_x(self.points_list)
        print_str = "分治算法得到点击加入点后的最短点对距离为：%f  最短点对的坐标是(%4d,%4d),(%4d,%4d)"%(self.get_closest_pairs(0, self.size-1), self.point_a['x'], self.point_a['y'], self.point_b['x'], self.point_b['y'])
        # print(print_str)
        self.insert_info(print_str+"\n")
        
    def brute_closest_pairs(self, points_list):
        init_distance = MAX_DISTANCE
        for i in range(self.size):
            for j in range(i+1, self.size):
                dis = self.get_distance(points_list[i], points_list[j])
                if dis < init_distance:
                    init_distance = dis
                    self.point_a = points_list[i]
                    self.point_b = points_list[j]
        print_str = "常规算法得到最终平面上最短点对距离是：%f  最短点对的坐标是(%4d,%4d),(%4d,%4d)"%(init_distance, self.point_a['x'], self.point_a['y'], self.point_b['x'], self.point_b['y'])
        # print(print_str)
        self.insert_info(print_str+"\n")

    #在文本框插入输出信息
    def insert_info(self, info):
        self.info_text.insert('end', info)

    #只使用分治算法进行最短点对的计算
    def compare(self):
        self.generate_random_points()

        start = time.clock()
        self.points_list = self.sort_x(self.points_list)
        print_str = "分治算法得到最终平面上最短点对距离是：%f  最短点对的坐标是(%4d,%4d),(%4d,%4d)"%(self.get_closest_pairs(0, self.size-1), self.point_a['x'], self.point_a['y'], self.point_b['x'], self.point_b['y'])
        end = time.clock()
        print("分治算法用时:%.4f" %(end - start))
        # print(print_str)
        self.insert_info(print_str+"\n")

        self.window.mainloop()
        # self.window.quit()

    def close_window(self):
        self.window.destroy()

        
if __name__ == '__main__':
    size = int(input("请输入平面上点的数量："))
    cp = ClosestPairs(size)
    cp.compare()
    
    