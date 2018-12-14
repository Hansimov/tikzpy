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
            '_anchor':   'c',
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

    def decorateWH(arg):
        @property
        def prop(self):
            self.calcFont()
            self.xb, self.yb, self.ww, self.hh, self.xa, self.ya = list(map(lambda x: round(CONTEXT.text_extents(self.text)[x], 2), [0, 1, 2, 3, 4, 5]))
            CONTEXT.stroke()
            wh_arg = {
                'width':    self.xa+self.xb,
                'height':   abs(self.ya+self.yb),
            }
            return wh_arg[arg]
        return prop

    for key in ['width', 'height']:
        exec(f"{key} = decorateWH('{key}')")

    # ---------- |----------------
    #   *    depends on     *
    # ---------- |----------------
    #   c        |    anchor, xy, nsew
    #   anchor   |     /
    #   xy       |    anchor, c, nsew
    #   nsew     |    anchor, c, xy
    # -----------|----------------

    # -----------|----------------
    #   change   |   influenced   
    # -----------|----------------
    #   c        |    xy, nsew
    #   anchor   |    c (-> nsew) (fix xy)
    #   xy       |    c (-> nsew)
    #   nsew     |    c (-> xy)
    # -----------|----------------

    # Note: 
    # 'anchor' has two meanings here:
    #   1. (1-char str) value of 'anchor' attribute/property
    #   2. (2-int list) collective name of 'n','s','e','w', ... attribute/property

    def decorateAnchor():
        @property
        def prop(self):
            # get anchor from _anchor
            return self._anchor
        @prop.setter
        def prop(self, val):
            # change anchor (fix xy) and set c (-> nsew)
            # val: 1-char str, (anchor)
            anchor_old = self._anchor
            anchor_new = val
            self._anchor = val
            # Do not use old xy to calc new c, 
            #   because it costs much time and gets wrong results.
            # Use old and new anchor to calc,
            #   although a bit more complicated, it is fast.
            x = getattr(self, anchor_old)[0]
            y = getattr(self, anchor_old)[1]

            nsew_list = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']
            tbrl_list = ['t', 'b', 'r', 'l', 'tr', 'tl', 'br', 'bl']

            if not val in nsew_list:
                val = nsew_list[tbrl_list.index(val)]

            anchor_dict = {
                'c':    [x,                y],
                'n':    [x,                y+self.height/2],
                's':    [x,                y-self.height/2],
                'e':    [x-self.width/2,   y],
                'w':    [x+self.width/2,   y],
                'ne':   [x-self.width/2,   y+self.height/2],
                'nw':   [x+self.width/2,   y+self.height/2],
                'se':   [x-self.width/2,   y-self.height/2],
                'sw':   [x+self.width/2,   y-self.height/2],
            }
            self.c = anchor_dict[val]
        return prop
    anchor = decorateAnchor()

    def decorateNSEW(arg):
        # arg: 'n', 's, 'e', 'w', '(n|s)(e|w)''
        @property
        def prop(self):
            # get nsew(=arg) from c and arg
            nsew_dict = {
                'c':    [self.c[0],                 self.c[1]],
                'n':    [self.c[0],                 self.c[1]-self.height/2],
                's':    [self.c[0],                 self.c[1]+self.height/2],
                'e':    [self.c[0]+self.width/2,    self.c[1]],
                'w':    [self.c[0]-self.width/2,    self.c[1]],
                'ne':   [self.c[0]+self.width/2,    self.c[1]-self.height/2],
                'nw':   [self.c[0]-self.width/2,    self.c[1]-self.height/2],
                'se':   [self.c[0]+self.width/2,    self.c[1]+self.height/2],
                'sw':   [self.c[0]-self.width/2,    self.c[1]+self.height/2],
            }
            return nsew_dict[arg]
        @prop.setter
        def prop(self, val):
            # change nsew and set c (-> xy)
            # val: 2-int list, (nsew)
            # same to xy setter
            val_dict = {
                'c':    [val[0],                val[1]],
                'n':    [val[0],                val[1]+self.height/2],
                's':    [val[0],                val[1]-self.height/2],
                'e':    [val[0]-self.width/2,   val[1]],
                'w':    [val[0]+self.width/2,   val[1]],
                'ne':   [val[0]-self.width/2,   val[1]+self.height/2],
                'nw':   [val[0]+self.width/2,   val[1]+self.height/2],
                'se':   [val[0]-self.width/2,   val[1]-self.height/2],
                'sw':   [val[0]+self.width/2,   val[1]-self.height/2],
            }
            self.c = val_dict[arg]
        return prop

    nsew_list = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']
    tbrl_list = ['t', 'b', 'r', 'l', 'tr', 'tl', 'br', 'bl']
    for i in range(len(nsew_list)):
        nsew_key = nsew_list[i]
        tbrl_key = tbrl_list[i]
        exec(f"{nsew_key} = decorateNSEW('{nsew_key}')")
        exec(f"{tbrl_key} = decorateNSEW('{nsew_key}')")


    def decorateXY(arg):
        # arg: 'x', 'y', 'xy'
        @property
        def prop(self):
            # get xy from nsew (which is got from c and anchor tag)
            xy_dict = {
                'x':    getattr(self, self._anchor)[0],
                'y':    getattr(self, self._anchor)[1],
                'xy':   getattr(self, self._anchor),
            }
            return xy_dict[arg]
        @prop.setter
        def prop(self, val):
            # change x,y,xy (fix anchor) and set c (-> nsew)
            # val: int or 2-ele list, (x, y, xy)
            val_dict = {
                'x':    [val, False | self.y],
                'y':    [False | self.x, val],
                'xy':   val,
            }
            val = val_dict[arg]
            anchor_dict = {
                'c':    [val[0],                val[1]],
                'n':    [val[0],                val[1]+self.height/2],
                's':    [val[0],                val[1]-self.height/2],
                'e':    [val[0]-self.width/2,   val[1]],
                'w':    [val[0]+self.width/2,   val[1]],
                'ne':   [val[0]-self.width/2,   val[1]+self.height/2],
                'nw':   [val[0]+self.width/2,   val[1]+self.height/2],
                'se':   [val[0]-self.width/2,   val[1]-self.height/2],
                'sw':   [val[0]+self.width/2,   val[1]-self.height/2],
            }
            xy_dict = {
                'x':    [anchor_dict[self.anchor][0], self.y | False],
                'y':    [self.x | False, anchor_dict[self.anchor][1]],
                'xy':   anchor_dict[self.anchor],
            }
            self.c = xy_dict[arg]
        return prop

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


