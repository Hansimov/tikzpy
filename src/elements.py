from tikzpyinit import *

class arc:
    def __init__(self, x=50, y=200, r=50, beg=0, end=pi):
        # self.id = len(ELEMENTS)
        ELEMENTS.append(self)
        # self.options = {}
        self.x = x
        self.y = y
        self.r = r
        self.beg = beg
        self.end = end

    def __setattr__(self, attr, value):
        # if attr != 'options' and attr != 'id':
            # print('set %s to %s' % (attr, value))
            # ELEMENTS[self.id] = self
        super().__setattr__(attr, value)

    def paint(self, CONTEXT):
        # print(self.__dict__)
        CONTEXT.arc(self.x, self.y, self.r, self.beg, self.end)
        CONTEXT.stroke()

class node:
    # Text in PyCairo - ZetCode
    #   http://zetcode.com/gfx/pycairo/text/
    def __init__(self, text='PYCAIRO', x=100, y=200, face="Arial Unicode MS", size=12):
        ELEMENTS.append(self)
        self.text = text
        self.x = x
        self.y = y
        self.face = face
        self.size = size

    def paint(self, CONTEXT):
        CONTEXT.move_to(self.x, self.y)
        CONTEXT.select_font_face(self.face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        CONTEXT.set_font_size(self.size)
        CONTEXT.show_text(self.text)
        # CONTEXT.fill()

