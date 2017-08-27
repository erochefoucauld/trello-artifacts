class Vert:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

class Line:
    def __init__(self, verts):
        self.begin = verts[0]
        self.end = verts[1]

class Rectangle:
    def __init__(self, verts):
        self.top_left = verts[0]
        self.top_right = verts[1]
        self.bottom_right = verts[0]
        self.bottom_left = verts[1]
        self.top = Line(verts[0], verts[1])
        self.right = Line(verts[1], verts[2])
        self.bottom = Line(verts[2], verts[3])
        self.left = Line(verts[3], verts[0])
