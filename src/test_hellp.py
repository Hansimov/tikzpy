from tikzpyinit import *
from elements import *

initTikzpy('test_hello.pdf')
arc1 = arc(x=50, y=30, r=100)
arc1.x = 100
arc2 = arc(x=300, y=300, beg=0.5*pi)
arc2.r = 50
arc2.end = 2*pi
outputImg()

print(len(ELEMENTS))
