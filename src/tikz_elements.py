import cairo
from math import *

# ELEMENTS, CONTEXT = [], []

def importTikzInit():
    global ELEMENTS, CONTEXT
    import tikz_init
    ELEMENTS, CONTEXT = tikz_init.ELEMENTS, tikz_init.CONTEXT

# ============================================= #
class vec(list):
    def __add__(self, other):
        vectmp = vec(self)
        for i in range(len(self)):
            vectmp[i] = self[i] + other[i]
        return vectmp

    __radd__ = __add__

    def __sub__(self, other):
        vectmp = vec(self)
        for i in range(len(self)):
            vectmp[i] = self[i] - other[i]
        return vectmp

    __rsub__ = __sub__

    def __mul__(self, other):
        vectmp = vec(self)
        for i in range(len(self)):
            vectmp[i] = self[i] * other
        return vectmp

    __rmul__ = __mul__

    def __truediv__(self, other):
        vectmp = vec(self)
        for i in range(len(self)):
            vectmp[i] = self[i] / other
        return vectmp

    __rtruediv__ = __truediv__

    def __neg__(self):
        vectmp = vec(self)
        for i in range(len(self)):
            vectmp[i] = -self[i]
        return vectmp

    @property
    def norm(self):
        square_sum = 0
        for i in range(len(self)):
            square_sum += self[i]**2
        norm = sqrt(square_sum)
        return norm

    @property
    def unit(self):
        vectmp = vec(self)
        norm = self.norm
        for i in range(len(self)):
            vectmp[i] /= norm
        return vectmp

    def dot(self, other):
        dot_product = 0
        for i in range(len(self)):
            dot_product += self[i] * other[i]
        return dot_product

    @property
    def orth(self):
        return vec([self[1], -self[0]])


# ============================================= #
class group:
    pass
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
        CONTEXT.save()
        CONTEXT.set_source_rgba(0.5, 0.0, 0.0, 0.5)
        CONTEXT.arc(self.x, self.y, self.r, self.begin, self.end)
        CONTEXT.stroke()
        CONTEXT.restore()


# ============================================= #
class circle:
    def __init__(self, **kwargs):
        importTikzInit()
        self.initArgs(kwargs)
        self.initFuncs()

    def initArgs(self, kwargs):
        default_args = {
        # others
            'is_append':    True,
        # position
            'c':        [0, 0],
            'r':        3,
        # stroke
            'is_stroke':    True,
            'stroke_rgba':  [0.0, 0.5, 1.0, 1.0],
        # fill
            'is_fill':      True,
            'fill_rgba':    [0.0, 1.0, 0.0, 0.8],
        }

        for key, val in default_args.items():
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)

    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)

    def paint(self):
        CONTEXT.save()
        CONTEXT.arc(*self.c, self.r, 0, 2.01*pi)
        # CONTEXT.set_source_rgba(*self.stroke_rgba)
        # CONTEXT.stroke_preserve()
        CONTEXT.set_source_rgba(*self.fill_rgba)
        CONTEXT.fill()
        CONTEXT.restore()


# ============================================= #
class tip:
    def __init__(self, **kwargs):
        importTikzInit()
        self.initArgs(kwargs)
        self.initFuncs()

    def initArgs(self, kwargs):
        default_args = {
        # others
            'is_append':    True,
        # shape
            'shape':    'stealth',
        # stroke
            'is_stroke':    True,
            'stroke_rgba':  [0.0, 0.0, 1.0, 1.0],
            'is_fill':      True,
            'fill_rgba':    [0.0, 0.0, 0.0, 1.0],
        # stealth
            'ax':           [[50, 50], [100, 50]],
            'len':          15,
            'ratio':        0.35,
            'angle':        pi*1/5,
        }

        for key, val in default_args.items():
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)

    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)

    @property
    def inset(self):
        return self.ratio * self.len
    @property
    def c(self):
        ax0, ax1 = vec(self.ax[0]), vec(self.ax[1])
        c = (1-self.ratio)*self.len * (ax0-ax1).unit + ax1
        # circle(c=c, r=1)
        return c
    @property
    def foot(self):
        ax0, ax1 = vec(self.ax[0]), vec(self.ax[1])
        foot = self.len * (ax0-ax1).unit + ax1
        # circle(c=foot, r=1)
        return foot
    @property
    def end(self):
        end = self.ax[1]
        # circle(c=end, r=1)
        return end

    @property
    def wing(self):
        wing = [0, 0]
        u = self.foot - self.end
        v = tan(self.angle/2) * u.orth.unit * self.len
        wing[0] = self.foot + v
        wing[1] = self.foot - v
        # circle(c=wing[0], r=1)
        # circle(c=wing[1], r=1)
        return wing

    def stroke(self):
        if self.is_stroke:
            if self.shape == 'stealth':
                CONTEXT.line_to(*self.end)
                CONTEXT.line_to(*self.wing[0])
                CONTEXT.line_to(*self.c)
                CONTEXT.line_to(*self.wing[1])
                CONTEXT.close_path()

            CONTEXT.set_source_rgba(*self.stroke_rgba)
            CONTEXT.set_line_width(0.2)
            if self.is_fill:
                CONTEXT.stroke_preserve()
            else:
                CONTEXT.stroke()

    def fill(self):
        if self.is_fill:
            CONTEXT.set_source_rgba(*self.fill_rgba)
            CONTEXT.fill()

    def paint(self):
        CONTEXT.save()
        self.stroke()
        self.fill()
        CONTEXT.stroke()
        CONTEXT.restore()


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
            'marks':        [],
            'points':       [],
            'controls':     [],
            'way':          '',
        # dot
            'is_dot':   False,
            'dot_rgba':  [0.0, 0.5, 1.0, 1.0],
        # arrow
            'is_arrow':       True,
        # stroke
            'is_stroke':    True,
            'is_smooth':    False,
            'smoothness':   0.25,
            'stroke_rgba':  [0.0, 0.5, 1.0, 1.0],
        # tip
            'tip':           tip(is_append=False),
        }

        for key, val in default_args.items():
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)

    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)

    def dot(self):
        if self.is_dot:
            for point in self.points:
                circle(c=point, r=2)
            for point in self.controls:
                circle(c=point, r=4)

    def calcControls(self):
        # num of points:    N
        # num of curves:    N-1
        # num of controls:  2*(N-2)
        # each curve depends on 2 points and 2 controls
        # points i, i+1, i+2 determine controls 2i, 2i+1
        # i: 0 -> N-3
        for i in range(len(self.points)-2):
            # Of course I can use numpy to simplify,
            #   but it is too heavy,
            #   and I want to keep dependencies as few as possible
            p1 = vec(self.points[i])
            p2 = vec(self.points[i+1])
            p3 = vec(self.points[i+2])

            v12 = p1 - p2
            v32 = p3 - p2

            vperp = (v12.unit + v32.unit).unit
            # vperp = (v12 + v32).unit

            w12 = vperp * vperp.dot(v12)
            w32 = vperp * vperp.dot(v32)

            u12 = v12 - w12
            u32 = v32 - w32

            c1 = self.smoothness * u12 + p2
            c2 = self.smoothness * u32 + p2

            # circle(c=c1, r=2, fill_rgba=[0, 0.5, 0, 1.0])
            # circle(c=c2, r=2, fill_rgba=[0.5, 0, 0, 1.0])
            # CONTEXT.move_to(*c1)
            # CONTEXT.line_to(*c2)
            if i == 0:
                x11 = c1 - p1
                c0 =  2*self.smoothness * x11 + p1
                self.controls.append(c0)
                self.controls.append(c1)
            else:
                self.controls.append(c1)

            if i == len(self.points) - 3:
                self.controls.append(c2)
                x23 = c2 - p3
                c3 = self.smoothness * x23 + p3
                self.controls.append(c3)
            else:
                self.controls.append(c2)

    def stroke(self):
        if self.is_stroke:
            CONTEXT.set_source_rgba(*self.stroke_rgba)
            CONTEXT.set_line_width(1)
            if self.is_smooth:
                self.calcControls()
                for i in range(len(self.points) - 1):
                    p1 = self.points[i]
                    p2 = self.points[i+1]

                    c1 = self.controls[2*i]
                    c2 = self.controls[2*i+1]
                    # circle(c=p1)
                    # circle(c=p2)

                    if i == len(self.points)-2 and self.is_arrow:
                        self.calcArrow()
                        p2 = self.tip.c
                    # if self.tip.len is too large,
                    # then the last curve will be strange
                    CONTEXT.move_to(*p1)
                    CONTEXT.curve_to(*c1, *c2, *p2)

            else:
                for point in self.points:
                    CONTEXT.line_to(*point)
            CONTEXT.stroke()

    def calcArrow(self):
        if self.is_smooth:
            if self.is_stroke:
                self.calcControls()
            self.tip.ax = [self.controls[-1], self.points[-1]]
        else:
            self.tip.ax = [self.points[-2], self.points[-1]]

    def arrow(self):
        if not self.is_stroke:
            self.calcArrow()
        self.tip.paint()

    def paint(self):
        CONTEXT.save()
        self.dot()
        self.stroke()
        self.arrow()
        CONTEXT.stroke()
        CONTEXT.restore()

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
            '_font_old':    -1,
            '_font_new':    0,
            'wh':           [0, 0],
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
        CONTEXT.set_font_size(self.font_size)
        CONTEXT.select_font_face(self.font_face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

    def updateWH(self):
        if self._font_old == self._font_new:
            pass
        elif self.text == '':
            self.wh = [0,0]
        else:
            self.setPaintFont()
            # Note: text_extents() takes most exec time of the whole program
            xb, yb, ww, hh, xa, ya = CONTEXT.text_extents(self.text)
            CONTEXT.stroke()
            self.wh[0] = round(xa+xb,      2)
            self.wh[1] = round(abs(ya+yb), 2)
            self._font_old = self._font_new
            # print(self._font_old, self._font_new)

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
            # exec(f"self._{arg} = val")

            _arg = '_' + arg
            # arg_dict = {
            #     'font_size': self._font_size,
            #     'font_face': self._font_face,
            #     'text':      self._text,
            # }
            setattr(self, _arg, val)

            self._font_new += 1
        return prop

    for key in ['text', 'font_size', 'font_face']:
        exec(f"{key} = decorateText('{key}')")

    def decorateWH(arg):
        # arg: 'width', 'height'
        @property
        def prop(self):
            self.updateWH()
            wh_arg = {
                'width':        self.wh[0],
                'height':       self.wh[1],
            }
            return wh_arg[arg]
        @prop.setter
        def prop(self, val):
            val_dict = {
                'width':    [val,          self.wh[1]],
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
        # xy = [self.c[0], self.c[1]]
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
            ssept, ssepb, ssepr, ssepl = self.ssep
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
        CONTEXT.save()
        self.write()
        self.stroke()
        self.fill()
        CONTEXT.stroke()
        # At the last line, I add stroke() to clear the current path from the cairo context,
        #   otherwise new elements will start from the end point of the previous node.
        # See:
        #   https://pycairo.readthedocs.io/en/latest/reference/context.html#cairo.Context.stroke
        CONTEXT.restore()

# ============================================= #
class newPage:
    def __init__(self, **kwargs):
        importTikzInit()
        self.initArgs(kwargs)
        self.initFuncs()

    def initArgs(self, kwargs):
        default_args = {
        # others
            'is_append':    True,
        }

        for key, val in default_args.items():
            setattr(self, key, val)
        for key, val in kwargs.items():
            setattr(self, key, val)

    def initFuncs(self):
        if self.is_append:
            ELEMENTS.append(self)

    def paint(self):
        CONTEXT.show_page()