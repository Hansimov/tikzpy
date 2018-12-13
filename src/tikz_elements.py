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
            'c':        [0, 0],
            # 'xy':       [0, 0],
            # 'anchor':   'c',
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

    def decorateCoordinate(idx):
        @property
        def prop(self):
            return self.c[idx]
        @prop.setter
        def prop(self, val):
            self.c[idx] = val
        return prop

    def decorateAnchor(arg):
        @property
        def prop(self):
            self.calcFont()
            self.xb, self.yb, self.ww, self.hh, self.xa, self.ya = list(map(lambda x: round(CONTEXT.text_extents(self.text)[x], 2), [0, 1, 2, 3, 4, 5]))
            CONTEXT.stroke()
            self.width, self.height = self.xa+self.xb, abs(self.ya+self.yb)
            anchor_dict = {
                # 'c':    [self.x, self.y],
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


    #     # for key in ['x', 'y', 'height', 'anchor']:
    #     #     if not key in self.__dict__:
    #     #         return
    #     @property
    #     def prop(self):

    #         return center2anchor_dict[arg]
    #     # @prop.setter
    #     # def prop(self, val):
    #     #     # getter(self)[0] = val[0]
    #     #     # getter(self)[1] = anchor_val[arg][1]
    #     #     pass
    #     return prop

    for key, val in {'x':0, 'y':1}.items():
        exec(f"{key} = decorateCoordinate({val})")

    for key in ['n','s', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
        exec(f"{key} = decorateAnchor('{key}')")

    def calcFont(self):
        # CONTEXT.select_font_face(self.face)
        font_args = {
            'font_size': CONTEXT.set_font_size(self.font_size),
            'font_face': CONTEXT.select_font_face(self.font_face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        }
        for key, val in font_args.items():
            if key in self.__dict__:
                val

    # def calcAnchor(self):
    #     self.calcFont()
    #     self.xb, self.yb, self.ww, self.hh, self.xa, self.ya = list(map(lambda x: round(CONTEXT.text_extents(self.text)[x], 2), [0, 1, 2, 3, 4, 5]))
    #     CONTEXT.stroke()
    #     self.width, self.height = self.xa+self.xb, abs(self.ya+self.yb)

    #     anchor_arg = {
    #         'c':    [self.x, self.y],
    #         'n':    [self.x, self.y+self.height/2],
    #         's':    [self.x, self.y-self.height/2],
    #         'e':    [self.x+self.width/2, self.y],
    #         'w':    [self.x-self.width/2, self.y],
    #         'ne':   [self.x+self.width/2, self.y+self.height/2],
    #         'en':   [self.x+self.width/2, self.y+self.height/2],
    #         'nw':   [self.x-self.width/2, self.y+self.height/2],
    #         'wn':   [self.x-self.width/2, self.y+self.height/2],
    #         'se':   [self.x+self.width/2, self.y-self.height/2],
    #         'es':   [self.x+self.width/2, self.y-self.height/2],
    #         'sw':   [self.x-self.width/2, self.y-self.height/2],
    #         'ws':   [self.x-self.width/2, self.y-self.height/2],
    #     }
    #     self.c = anchor_arg[self.anchor]
    #     self.calcAnchorFromCenter()

    # def calcAnchorFromCenter(self):
    #         self.n = [self.c[0], self.c[1]-self.height/2]
    #         self.s = [self.c[0], self.c[1]+self.height/2]
    #         self.e = [self.c[0]+self.width/2, self.c[1]]
    #         self.w = [self.c[0]-self.width/2, self.c[1]]
    #         self.ne = self.en = [self.e[0], self.n[1]]
    #         self.nw = self.wn = [self.w[0], self.n[1]]
    #         self.se = self.es = [self.e[0], self.s[1]]
    #         self.sw = self.ws = [self.w[0], self.s[1]]

    # def calcColor(self):
        # pass

    def place(self):
        CONTEXT.move_to(self.x, self.y)

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

