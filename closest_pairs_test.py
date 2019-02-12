# coding=utf-8
"""
Created on 2019.2.10
@author: 刘祥
分治求最短点对算法参考博客：https://blog.csdn.net/Lytning/article/details/25370169
"""
import numpy as np
import random
import math

from operator import itemgetter #用来对字典列表根据特定属性进行排序

import time
import copy

MAX_DISTANCE = float('inf')
class ClosestPairs(object):

    def __init__(self, size=1000, total_w=10000, total_h=10000, canvas_w=1200, canvas_h=700):
        self.size = size

        self.dot_radius = 2
        self.total_w = total_w
        self.total_h = total_h

        #可选坐标集合
        # self.x_list = list(range(self.dot_radius, total_w - self.dot_radius))
        # self.y_list = list(range(self.dot_radius, total_h - self.dot_radius))
        #实际坐标集合
        # 使用random模块中的random.sample函数产生一个数值范围内的不重复的随机数
        # self.posx_list = random.sample(self.x_list, self.size)
        # self.posy_list = random.sample(self.y_list, self.size)
        self.posx_list = []
        self.posy_list = []

        #声明点列表
        self.points_list = []
        # self.temp_points_list = []  #存储points_list按照x和y属性排序的结果

        #存储最近的两个点
        self.point_a = {}
        self.point_b = {}

        #为了寻找最近点对，存储当前的距离
        self.curr_distance = MAX_DISTANCE


    def generate_random_points(self):    
        #创建随机点函数会包括重复点
        self.posx_list = np.random.random_integers(self.dot_radius, self.total_w - self.dot_radius, size=self.size)
        self.posy_list = np.random.random_integers(self.dot_radius, self.total_w - self.dot_radius, size=self.size)
        for i in range(self.size):
            point = {}
            point["x"] =  self.posx_list[i]
            point["y"] =  self.posy_list[i]
            self.points_list.append(point)
            

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
    
    def brute_closest_pairs(self, points_list):
        init_distance = MAX_DISTANCE
        for i in range(self.size):
            for j in range(i+1, self.size):
                dis = self.get_distance(points_list[i], points_list[j])
                if dis < init_distance:
                    init_distance = dis
                    self.point_a = points_list[i]
                    self.point_b = points_list[j]
        print_str = "常规算法得到最终平面上最短点对距离是：%f  最短点对的坐标是(%3d,%3d),(%3d,%3d)"%(init_distance, self.point_a['x'], self.point_a['y'], self.point_b['x'], self.point_b['y'])
        # print(print_str)
        # self.insert_info(print_str+"\n")


    #比较不同数据规模下两种算法的用时
    def compare(self):
        # size_list = [10, 100, 1000, 10**4]
        size_list = [10**5, 10**6]
        for size in size_list:
            print("数据量为%d时两种算法的运行时间如下："%size)
            self.size = size
            self.generate_random_points()

            # start = time.clock()
            # self.brute_closest_pairs(copy.deepcopy(self.points_list))       #传参得穿拷贝对象
            # end = time.clock()
            # print("常规算法用时:%.4f" %(end - start))

            start = time.clock()
            self.points_list = self.sort_x(self.points_list)
            print_str = "分治算法得到最终平面上最短点对距离是：%f  最短点对的坐标是(%3d,%3d),(%3d,%3d)"%(self.get_closest_pairs(0, self.size-1), self.point_a['x'], self.point_a['y'], self.point_b['x'], self.point_b['y'])
            end = time.clock()
            print("分治算法用时:%.4f" %(end - start))
            # print(print_str)

        

if __name__ == '__main__':
    # size = int(input("请输入点的数量："))
    cp = ClosestPairs()
    cp.compare()
    
    