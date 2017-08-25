import numpy as np
from numpy import linalg
import cairocffi as cairo
import scraper
import tri_builder as tb

#Get all of the relevant information from the scraper
lists = scraper.GetLists('Test Show')

#Build the pyramid around this information
y_loc = 15
x_loc = 5
surface = cairo.PDFSurface('artifact.pdf', 800, 600)
context = cairo.Context(surface)

with context:
    context.set_source_rgb(1,1,1)
    context.paint()

#card text
context.set_source_rgb(0,0,0)
context.move_to(x_loc, y_loc)
context.set_font_size(12)
context.select_font_face('Garamond',
        cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
for item in lists:
    for card in item.list_cards():
        context.show_text(card.name)
        y_loc += 15
        context.move_to(x_loc, y_loc)
    x_loc += 20

#pyramid
point_one = np.array((400, 20))
point_two = np.array((780, 580))
point_three = np.array((20, 580))

context.set_line_width(5)

tri = tb.BuildTriangle(point_one, point_two, point_three, lists)

context.move_to(tri.point_one[0], tri.point_one[1])
context.line_to(tri.point_two[0], tri.point_two[1])
context.line_to(tri.point_three[0], tri.point_three[1])
context.close_path()

context.stroke()

context.set_line_width(2.5)
for level in tri.levels:
    print(level.point_one)
    for level in tri.levels:
        x = level.point_one[0]
        y = level.point_one[1]
        context.move_to(level.point_one[0], level.point_one[1])
        print(level.point_one)
        print(level.point_two)
        context.line_to(level.point_two[0], level.point_two[1])

context.stroke()
