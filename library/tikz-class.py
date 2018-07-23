

# How to process units?

'''
# \draw (0,0) circle [radius=70pt];
# 1> c = circle(0, 0, 30).draw()
# 2> c = circle([0, 0]).radius(30).draw
# 2> c = circle(0, 0)
     c.r = 30
     c.draw()
     c.r = 40
     c.draw() # replace (or copy?) the previous one
'''

class circle:
    def __init__(self, x=0, y=0, r=0):
        self.x, self.y = x, y
        self.r = r

        self.tex = ''

# \draw (0,-30) -- (0,70);
# 1> p = path([0,-30], [0,30]).draw()
# 2> p = path([0,-30]).append([0,30])
class path:
    def __init__(self, *points):
        self.tex = ''

class ElementsList:
    eid = 0
    def __init__(self, eid=0, etype='node'):
        pass

