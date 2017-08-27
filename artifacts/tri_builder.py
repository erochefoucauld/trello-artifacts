import scraper
from rectangle import Vert, Line, Rectangle
import vector_math as vm

def BuildSegmentRect(top_line, bottom_line, width):
    top_left = top_line.begin
    top_right = Vert(top_line.begin.x + width, top_line.begin.y)
    bot_right = Vert(top_right.x, bottom_line.begin.y)
    bot_left = Vert(top_right.x, bot_right.y)
    verts = (top_left, top_right, bot_right, bot_left)
    rect = Rectangle(verts)
    return rect

class Segment:
    def __init__(self, rect, string):
        self.rectangle = rect
        self.text = string 

class Level:
    def __init__(self, top, bottom):
        self.segments = []
        self.top = top
        self.bottom = bottom

    def BuildSegments(self, cards):
        #if((0,0,0,0) != self.constraints and len(cards) > 0):
            #width_iterator = (self.bottom[0][0] - self.constraints[1][0]) / len(cards)
            #width = width_iterator
        card_iterator = len(cards) - 1
        for card in cards:
            rect = None
            #first segment
            if(self.top == None):
                temp_begin = Vert((0,0))
                temp_end = Vert((0,0))
                verts = []
                verts.append(temp_begin)
                verts.append(temp_end)
                temp_top = Line(verts)
                rect = BuildSegmentRect(temp_top, self.bottom, 0)
            #middle segments
            if(self.top and card_iterator > 0):
                rect = BuildSegmentRect(self.top, self.bottom, width)
               
            segment = Segment(rect, card.name)
            width += width_iterator
            self.segments.append(segment)
            card_iterator -= 1

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
        count = 0
        constraints = None
        for item in lists:
            #get number of cards for segments
            x1 += v1[0]
            y1 += v1[1]
            x2 += v2[0]
            y2 += v2[1]
            verts = []
            beg = Vert((x1, y1))
            end = Vert((x2, y2))
            verts.append(beg)
            verts.append(end)
            bottom_line = verts
            top_line = constraints
            level = Level(top_line, bottom_line)
            level.BuildSegments(item.list_cards())
            self.levels.append(level)
            constraints = bottom_line

def BuildTriangle(point_one, point_two, point_three,
        lists):
    triangle = Triangle()
    triangle.point_one = point_one
    triangle.point_two = point_two
    triangle.point_three = point_three
    triangle.num_levels = len(lists)
    triangle.side_one = vm.CreateVector(point_one, point_two)
    triangle.side_three = vm.CreateVector(point_one, point_three)
    triangle.point_one_norm = vm.Normalize(triangle.side_one)
    triangle.point_two_norm = vm.Normalize(triangle.side_three)
    triangle.distance = vm.Distance(point_one, point_two)

    triangle.BuildLevels(lists)

    return triangle
