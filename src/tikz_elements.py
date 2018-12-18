import cairo
from math import *

# ELEMENTS, CONTEXT = [], []

def importTikzInit():
    global ELEMENTS, CONTEXT
    import tikz_init
    ELEMENTS, CONTEXT = tikz_init.ELEMENTS, tikz_init.CONTEXT

# ============================================= #
class arc:
    def __init__(self, append=True, x=100, y=100, r=50, begin=0, end=2.01*pi):
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
        CONTEXT.arc(self.x, self.y, self.r, self.begin, self.end)
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
class line:
    def __init__(self, **kwargs):
        importTikzInit()
        self.initArgs(kwargs)
        self.initFuncs()

    def initArgs(self, kwargs):
        default_args = {
        # others
            'is_append':    True,
        # position
            'begin':        [0, 0],
            'end':          [100, 100],
        # stroke
            'is_stroke':    True,
            'stroke_rgba':  [0.0, 0.5, 1.0, 1.0],
        }

        for key, val in default_args.items():
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)


    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)

    def stroke(self):
        if self.is_stroke:
            CONTEXT.set_source_rgba(*self.stroke_rgba)
            CONTEXT.set_line_width(2)
            CONTEXT.line_to(*self.begin)
            CONTEXT.line_to(*self.end)
            CONTEXT.line_to(150,200)
            CONTEXT.stroke()

    def paint(self):
        self.stroke()
        CONTEXT.stroke()

# ============================================= #

nsew_list = ['c', 'n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']
tbrl_list = ['c', 't', 'b', 'r', 'l', 'tr', 'tl', 'br', 'bl']

def nsewDict(w,h):
    anchor_dict = {
        'c':    [0,     0],
        'n':    [0,     -h/2],
        's':    [0,     +h/2],
        'e':    [+w/2,  0],
        'w':    [-w/2,  0],
        'ne':   [+w/2,  -h/2],
        'nw':   [-w/2,  -h/2],
        'se':   [+w/2,  +h/2],
        'sw':   [-w/2,  +h/2],
    }
    return anchor_dict

def asepDict(asepn, aseps, asepe, asepw):
    asep_dict = {
        'c':    [0,      0],
        'n':    [0,      -asepn],
        's':    [0,      +aseps],
        'e':    [+asepe, 0],
        'w':    [-asepw, 0],
        'ne':   [+asepe, -asepn],
        'nw':   [-asepw, -asepn],
        'se':   [+asepe, +aseps],
        'sw':   [-asepw, +aseps],
    }
    return asep_dict




# ============================================= #
class node:
    # Text in PyCairo - ZetCode
    #   http://zetcode.com/gfx/pycairo/text/
    def __init__(self, **kwargs):
        importTikzInit()
        self.initArgs(kwargs)
        self.initFuncs()

    # - Initialize args
    # - Set args with inputs
    # - Do something which in the args list

    def initArgs(self, kwargs):
        default_args = {
        # others
            'is_append':    True,
        # text
            'is_write':     True,
            '_text':        '',
            '_font_size':   20,
            '_font_face':   'Arial Unicode MS',
            'wh':          [0, 0],
            'text_rgba':    [0.0, 0.0, 0.5, 1.0],
        # position
            '_anchor':      'c',
            '_xy':          [0, 0],
            'c':            [0, 0],
            'ssep':         [10,10,10,10], # stroke sep: nsew/tbrl
            'asep':         [25,25,25,25], # anchor sep: nsew/tbrl
        # fill
            'is_fill':     False,
            'fill_rgba':   [0.5, 0.0, 0.0, 1.0],
        # stroke
            'is_stroke':   False,
            'stroke_rgba': [0.0, 0.5, 0.0, 1.0],
        }

        for key, val in default_args.items():
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)

    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)


    def setPaintFont(self):
        # CONTEXT.select_font_face(self.face)
        font_args = {
            'font_size': CONTEXT.set_font_size(self.font_size),
            'font_face': CONTEXT.select_font_face(self.font_face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        }
        for key, val in font_args.items():
            if key in self.__dict__:
                val

    def decorateText(arg):
        # arg: 'text', 'font_size', 'font_face'
        @property
        def prop(self):
            # get infomation of text
            arg_dict = {
                'font_size': self._font_size,
                'font_face': self._font_face,
                'text':      self._text,
            }
            return arg_dict[arg]
        @prop.setter
        def prop(self, val):
            # val: int (font_size) / str (font_face) / str (text)
            exec(f"self._{arg} = val")
            val_dict = {
                'font_size': [val,             self._font_face, self._text],
                'font_face': [self._font_size, val,             self._text],
                'text':      [self._font_size, self._font_face, val],
            }
            arg_list = val_dict[arg]

            if self.text == '':
                self.width, self.height = 0, 0
            else:
                CONTEXT.set_font_size(arg_list[0])
                CONTEXT.select_font_face(arg_list[1], cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                # Note: text_extents() takes most exec time of the whole program
                self.xb, self.yb, self.ww, self.hh, self.xa, self.ya = list(map(lambda x: CONTEXT.text_extents(arg_list[2])[x], [0, 1, 2, 3, 4, 5]))
                CONTEXT.stroke()
                self.width  = round(self.xa+self.xb,      2)
                self.height = round(abs(self.ya+self.yb), 2)
        return prop

    for key in ['text', 'font_size', 'font_face']:
        exec(f"{key} = decorateText('{key}')")

    def decorateWH(arg):
        # arg: 'width', 'height'
        @property
        def prop(self):
            wh_arg = {
                'width':        self.wh[0],
                'height':       self.wh[1],
            }
            return wh_arg[arg]
        @prop.setter
        def prop(self, val):
            val_dict = {
                'width':    [val,           self.wh[1]],
                'height':   [self.wh[0],   val],
            }
            self.wh = val_dict[arg]
            # This line is to update c
            self.anchor = self.anchor
        return prop

    for key in ['width', 'height']:
        exec(f"{key} = decorateWH('{key}')")

    def decorateASEP(arg):
        # arg: 'asep(n|s|e|w)'
        @property
        def prop(self):
            idx = ['n','s','e','w'].index(arg[4])
            return self.asep[idx]
        @prop.setter
        def prop(self, val):
            idx = ['n','s','e','w'].index(arg[4])
            self.asep[idx] = val
        return prop

    for i in range(len(nsew_list[1:5])):
        asep_nsew_key = 'asep' + nsew_list[1:5][i]
        asep_tbrl_key = 'asep' + tbrl_list[1:5][i]
        exec(f"{asep_nsew_key} = decorateASEP('{asep_nsew_key}')")
        exec(f"{asep_tbrl_key} = decorateASEP('{asep_nsew_key}')")

    def decorateXY(arg):
        # arg: 'x', 'y', 'xy'
        @property
        def prop(self):
            # get xy from nsew (which is got from c and anchor tag)
            xy_dict = {
                'x':    self._xy[0],
                'y':    self._xy[1],
                'xy':   self._xy,
            }
            return xy_dict[arg]
        @prop.setter
        def prop(self, val):
            # change x,y,xy (fix anchor) and set c (-> nsew)
            # val: int or 2-ele list, (x, y, xy)
            val_dict = {
                'x':    [val, self._xy[1]],
                'y':    [self._xy[0], val],
                'xy':   val,
            }
            val_list = val_dict[arg]
            self._xy = val_dict[arg]

            nsew_dict = nsewDict(*self.wh)
            asep_dict = asepDict(*self.asep)

            anchor = self.anchor
            if not anchor in nsew_list:
                anchor = nsew_list[tbrl_list.index(anchor)]

            self.c = list(map(lambda a,b,c: a-b-c, val_list, nsew_dict[anchor], asep_dict[anchor]))
        return prop

    for key in ['x', 'y', 'xy']:
        exec(f"{key} = decorateXY('{key}')")

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
            # val: 1or2-char str, (anchor)
            self._anchor = val

            if not val in nsew_list:
                val = nsew_list[tbrl_list.index(val)]

            nsew_dict = nsewDict(*self.wh)
            asep_dict = asepDict(*self.asep)

            self.c = list(map(lambda a,b,c: a-b-c, self._xy, nsew_dict[val], asep_dict[val]))
        return prop

    anchor = decorateAnchor()

    def decorateNSEW(arg):
        # arg: 'n', 's, 'e', 'w', '(n|s)(e|w)''
        @property
        def prop(self):
            # get nsew(=arg) from c and arg
            nsew_dict = nsewDict(*self.wh)
            asep_dict = asepDict(*self.asep)
            nsew_val = list(map(lambda a,b,c: a+b+c, self.c, nsew_dict[arg], asep_dict[arg]))
            return nsew_val
        @prop.setter
        def prop(self, val):
            # change nsew and set c (-> xy)
            # val: 2-int list, (nsew)
            # same to xy setter

            nsew_dict = nsewDict(*self.wh)
            asep_dict = asepDict(*self.asep)
            self.c = list(map(lambda a,b,c: a-b-c, val, nsew_dict[arg], asep_dict[arg]))
        return prop

    for i in range(len(nsew_list[1:])):
        # Do not decorate 'c'
        nsew_key = nsew_list[1:][i]
        tbrl_key = tbrl_list[1:][i]
        exec(f"{nsew_key} = decorateNSEW('{nsew_key}')")
        exec(f"{tbrl_key} = decorateNSEW('{nsew_key}')")


    def place(self):
        xy = [self.c[0]-self.width/2, self.c[1]+self.height/2]
        CONTEXT.move_to(*xy)

    def write(self):
        if self.is_write:
            self.place()
            self.setPaintFont()
            CONTEXT.set_source_rgba(*self.text_rgba)
            CONTEXT.show_text(self.text)

    def stroke(self):
        if self.is_stroke:
            CONTEXT.set_source_rgba(0, 0.5, 0, 1)
            CONTEXT.set_line_width(2)
            # nsew/tbrl
            ssept, ssepb, ssepr, ssepl = list(map(lambda i: self.ssep[i], [0, 1, 2, 3]))
            rectxy = [self.c[0]-ssepl-self.width/2, self.c[1]-self.height/2-ssept]
            rectwh = [self.width+ssepl+ssepr, self.height+ssept+ssepb]
            CONTEXT.rectangle(*rectxy, *rectwh)
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
        # importTikzInit()
        self.write()
        self.stroke()
        self.fill()
        CONTEXT.stroke()
        # At the last line, I add stroke() to clear the current path from the cairo context,
        #   otherwise new elements will start from the end point of the previous node.
        # See:
        #   https://pycairo.readthedocs.io/en/latest/reference/context.html#cairo.Context.stroke

