import cairo
from math import *

# ELEMENTS, CONTEXT = [], []

def importTikzInit():
    global ELEMENTS, CONTEXT
    import tikz_init
    ELEMENTS, CONTEXT = tikz_init.ELEMENTS, tikz_init.CONTEXT


# ============================================= #
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


# ============================================= #
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


# ============================================= #



# ============================================= #
class node:
    # Text in PyCairo - ZetCode
    #   http://zetcode.com/gfx/pycairo/text/
    def __init__(self, **kwargs):
        importTikzInit()
        self.initArgs(kwargs)
        self.initFuncs()

# Initialize args
# Set args with inputs
# Do something which in the args list

    def initArgs(self, kwargs):
        default_args = {
        # others
            'is_append':    True,
        # text
            'is_write':      True,
            'text':         'TikZpy',
            'text_rgba':    [0.0, 0.0, 0.5, 1.0],
            'font_size':    20,
            'font_face':    'Arial Unicode MS',
        # position
            'anchor':   'c',
            'c':        [0, 0],
        # fill
            'is_fill':      False,
            'fill_rgba':   [0.5, 0.0, 0.0, 1.0],
        # stroke
            'is_stroke':    False,
            'stroke_rgba': [0.0, 0.5, 0.0, 1.0],
        }

        for key, val in default_args.items():
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)

    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)

    # def __setattr__(self, attr, val):
    #     # if attr != 'options' and attr != 'id':
    #         # print('set %s to %s' % (attr, value))
    #         # ELEMENTS[self.id] = self
    #     super().__setattr__(attr, val)
    #     trig_args ={
    #     # x,y,xy, anchor -> c -> n,s,w,e
    #         'x':       self.updateXY('x', val),
    #         'y':       self.updateXY('y', val),
    #         'xy':      self.updateXY('xy', val),
    #         'anchor':  self.updateAnchor('c', val),
    #     # rgb, hsl, name, hex, -> rgba
    #         'stroke_color': self.updateColor(),
    #         'fill_color':   self.updateColor(),
    #         'text_color':   self.updateColor(),
    #     }
    #     if attr in trig_args:
    #         trig_args[attr]

    def decorateAnchor(arg):
        @property
        def prop(self):
            self.calcFont()
            self.xb, self.yb, self.ww, self.hh, self.xa, self.ya = list(map(lambda x: round(CONTEXT.text_extents(self.text)[x], 2), [0, 1, 2, 3, 4, 5]))
            CONTEXT.stroke()
            self.width, self.height = self.xa+self.xb, abs(self.ya+self.yb)
            anchor_dict = {
                'n':    [self.c[0], self.c[1]-self.height/2],
                's':    [self.c[0], self.c[1]+self.height/2],
                'e':    [self.c[0]+self.width/2, self.c[1]],
                'w':    [self.c[0]-self.width/2, self.c[1]],
                'ne':   [self.c[0]+self.width/2, self.c[1]-self.height/2],
                'nw':   [self.c[0]-self.width/2, self.c[1]-self.height/2],
                'se':   [self.c[0]+self.width/2, self.c[1]+self.height/2],
                'sw':   [self.c[0]-self.width/2, self.c[1]+self.height/2],
            }
            return anchor_dict[arg]
        return prop

    def decorateXY(arg):
        @property
        def prop(self):
            xy_dict = {
                'x':    getattr(self, self.anchor)[0],
                'y':    getattr(self, self.anchor)[1],
                'xy':   getattr(self, self.anchor),
            }
            return xy_dict[arg]
        return prop

    for key in ['n','s', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
        exec(f"{key} = decorateAnchor('{key}')")

    for key in ['x', 'y', 'xy']:
        exec(f"{key} = decorateXY('{key}')")

    def calcFont(self):
        # CONTEXT.select_font_face(self.face)
        font_args = {
            'font_size': CONTEXT.set_font_size(self.font_size),
            'font_face': CONTEXT.select_font_face(self.font_face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        }
        for key, val in font_args.items():
            if key in self.__dict__:
                val

    def place(self):
        CONTEXT.move_to(self.sw[0], self.sw[1])

    def write(self):
        if self.is_write:
            self.place()
            self.calcFont()
            CONTEXT.set_source_rgba(*self.text_rgba)
            CONTEXT.show_text(self.text)

    def stroke(self):
        if self.is_stroke:
            CONTEXT.set_source_rgba(*self.stroke_rgba)
            if self.is_fill:
                CONTEXT.stroke_preserve()
            else:
                CONTEXT.stroke()

    # def calcColor(self):
    #     # color_name, rgb, rgba, cmyk, hsl, hex
    #     # ['name','white!black']
    #     # ['hex', '00ff00']
    #     # ['rgb(a)', 255, [0, 255, 128]]

    def fill(self):
        if self.is_fill:
            CONTEXT.set_source_rgba(*self.fill_rgba)
            CONTEXT.fill()

    def paint(self):
        importTikzInit()
        self.write()
        self.stroke()
        self.fill()
        CONTEXT.stroke()
        # At the last line, I add stroke() to clear the current path from the cairo context,
        #   otherwise new elements will start from the end point of the previous node.
        # See:
        #   https://pycairo.readthedocs.io/en/latest/reference/context.html#cairo.Context.stroke


