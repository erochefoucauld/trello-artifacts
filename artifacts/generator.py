import cairocffi as cairo
import scraper

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
