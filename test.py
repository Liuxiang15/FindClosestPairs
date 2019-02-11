import numpy as np 
points_list = []
while len(points_list) < 10:
            point = {}
            point["x"] =  np.random.random_integers(0, 100)
            point["y"] =  np.random.random_integers(0, 100)
            # print(i,end=" ")
            if not point in points_list:
                points_list.append(point)
print(points_list)