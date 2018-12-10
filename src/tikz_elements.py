import cairo
from math import *

# ELEMENTS, CONTEXT = [], []

def importTikzInit():
    global ELEMENTS, CONTEXT
    import tikz_init
    ELEMENTS, CONTEXT = tikz_init.ELEMENTS, tikz_init.CONTEXT

class arc:
    def __init__(self, append=True, x=100, y=100, r=50, beg=0, end=2.01*pi):
        importTikzInit()
        if append:
            ELEMENTS.append(self)
        self.x = x
        self.y = y
        self.r = r
        self.beg = beg
        self.end = end

    # def __setattr__(self, attr, value):
    #     # if attr != 'options' and attr != 'id':
    #         # print('set %s to %s' % (attr, value))
    #         # ELEMENTS[self.id] = self
    #     super().__setattr__(attr, value)

    def paint(self):
        importTikzInit()
        # CONTEXT.move_to(self.x, self.y)
        CONTEXT.set_source_rgba(0.5, 0.0, 0.0, 0.5)
        CONTEXT.arc(self.x, self.y, self.r, self.beg, self.end)
        CONTEXT.stroke()

class circle:
    def __init__(self, append=True, x=100, y=100, r=50):
        importTikzInit()
        if append:
            ELEMENTS.append(self)
        self.x = x
        self.y = y
        self.r = r

    def paint(self):
        importTikzInit()
        # CONTEXT.move_to(self.x, self.y)
        CONTEXT.set_source_rgba(0.0, 0.5, 0.0, 0.5)
        CONTEXT.arc(self.x, self.y, self.r, 0, 2.01*pi)
        CONTEXT.stroke_preserve()
        CONTEXT.set_source_rgba(0.0, 0.0, 0.5, 0.5)
        CONTEXT.fill()

class node:
    # Text in PyCairo - ZetCode
    #   http://zetcode.com/gfx/pycairo/text/
    def __init__(self, append=True, text='PYCAIRO', x=100, y=200, face="Arial Unicode MS", size=12):
        importTikzInit()
        if append:
            ELEMENTS.append(self)
        self.text = text
        self.x = x
        self.y = y
        self.face = face
        self.size = size
        self.calcAnchor()

    def boxize(self):
        # CONTEXT.select_font_face(self.face)
        CONTEXT.select_font_face(self.face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        CONTEXT.set_font_size(self.size)
        CONTEXT.move_to(self.x, self.y)

    def calcAnchor(self):
        self.boxize()
        self.xb, self.yb, self.ww, self.hh, self.xa, self.ya = list(map(lambda x: round(CONTEXT.text_extents(self.text)[x], 2), [0, 1, 2, 3, 4, 5]))
        CONTEXT.stroke()
        self.width, self.height = self.xa+self.xb, abs(self.ya+self.yb)
        self.n = [self.x+self.width/2,  self.y-self.height]
        self.s = [self.x+self.width/2,  self.y]
        self.e = [self.x+self.width,    self.y-self.height/2]
        self.w = [self.x,               self.y-self.height/2]
        self.ne = self.en = [self.e[0], self.n[1]]
        self.nw = self.wn = [self.w[0], self.n[1]]
        self.se = self.es = [self.e[0], self.s[1]]
        self.sw = self.ws = [self.w[0], self.s[1]]
        self.c = [self.n[0], self.e[1]]

    def paint(self):
        importTikzInit()
        self.boxize()
        CONTEXT.show_text(self.text)
        print(CONTEXT.text_extents(self.text))
        CONTEXT.stroke()
        # At the last line, I add stroke() to clear the current path from the cairo context,
        #   otherwise new elements will start from the end point of the previous node.
        # See:
        #   https://pycairo.readthedocs.io/en/latest/reference/context.html#cairo.Context.stroke
