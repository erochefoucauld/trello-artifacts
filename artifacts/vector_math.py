import numpy as np

def Distance(point_one, point_two):
    x1 = point_one[0]
    y1 = point_one[1]
    x2 = point_two[0]
    y2 = point_two[1]
    x = x2 - x1
    y = y2 - y1
    x = x * x
    y = y * y
    v = x + y
    distance = np.sqrt(v)
    return distance
    
def CreateVector(point_one, point_two):
   x = point_two[0] - point_one[0]
   y = point_two[1] - point_one[1]
   vector = (x, y)
   return vector

def Magnitude(vector):
    x = vector[0] * vector[0]
    y = vector[1] * vector[1]
    v = x + y
    return np.sqrt(v)

def Normalize(vector):
    mag = Magnitude(vector)
    x = vector[0]/mag
    y = vector[0]/mag
    v = (x,y)
    return v

