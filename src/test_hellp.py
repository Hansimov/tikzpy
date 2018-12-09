from tikzpyinit import *
from elements import *

initTikzpy('test_hello.pdf')
arc1 = arc(x=50, y=30, r=100)
arc1.x = 100
arc2 = arc(x=300, y=300, beg=0.5*pi)
arc2.r = 60
arc2.end = 1.9 * pi
text1 = node(x=100, y=300, text='hello', face='Consolas')
outputImg()
