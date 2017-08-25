import numpy as np
from numpy import linalg as la
import scraper

#to get a unit vector
#find vector between two points
#normalize the vector
#divide the vector by the normalized vector
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

class Segment:
    num = 0
    point_one = ()
    point_two = ()

class Level:
    num_segments = 0
    segments = ()
    point_one = ()
    point_two = ()
    def BuildSegments(num_cards):
        s = 0

class Triangle:
    point_one = ()
    point_one_norm = ()
    point_two = ()
    point_two_norm = ()
    point_three = ()
    side_one = ()
    side_two = ()
    side_three = ()
    levels = list()
    num_levels = 0
    distance = 0

    def BuildLevels(self, lists):
        x1 = x2 = self.point_one[0]
        y1 = y2 = self.point_one[1]
        v1 = (self.side_one[0] / self.num_levels, self.side_one[1]/self.num_levels)
        v2 = (self.side_three[0] / self.num_levels, self.side_three[1]/self.num_levels)
        for item in lists:
            #get number of cards for segments
            level = Level()
            x1 += v1[0]
            y1 += v1[1]
            x2 += v2[0]
            y2 += v2[1]
            level.point_one = (x1, y1)
            level.point_two = (x2, y2)
            self.levels.append(level)


def BuildTriangle(point_one, point_two, point_three,
        lists):
    triangle = Triangle()
    triangle.point_one = point_one
    triangle.point_two = point_two
    triangle.point_three = point_three
    triangle.num_levels = len(lists)
    triangle.side_one = CreateVector(point_one, point_two)
    triangle.side_three = CreateVector(point_one, point_three)
    triangle.point_one_norm = Normalize(triangle.side_one)
    triangle.point_two_norm = Normalize(triangle.side_three)
    print(triangle.point_one_norm)
    triangle.distance = Distance(point_one, point_two)
    print(triangle.distance)

    triangle.BuildLevels(lists)

    return triangle
