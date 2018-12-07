from tikzpyinit import *

class arc():
    def __init__(self, x=50, y=200, r=50, beg=0, end=pi):
        # self.id = len(ELEMENTS)
        ELEMENTS.append(self)
        self.options = {}
        self.x = x
        self.y = y
        self.r = r
        self.beg = beg
        self.end = end

    def __setattr__(self, attr, value):
        if attr != 'options' and attr != 'id':
            print('set %s to %s' % (attr, value))
            # ELEMENTS[self.id] = self
        super().__setattr__(attr, value)

    def paint(self, CONTEXT):
        print(self.__dict__)
        CONTEXT.arc(self.x, self.y, self.r, self.beg, self.end)
        CONTEXT.stroke()


