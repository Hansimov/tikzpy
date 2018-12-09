from tikzpyinit import *
from elements import *

initTikzpy('test_hello.pdf', width=600, height=500)
arc1 = arc(x=50, y=50, r=40)
arc2 = arc(x=150, y=90, beg=0.5*pi)
arc2.r, arc2.end = 60, 1.9 * pi
xxx = 'π * 123 + 456 β∮ 天地玄黄，宇宙洪荒'
node1 = node(x=20, y=200, size=20, text=xxx, face='Source Han Sans HW SC')
node2 = node(x=20, y=223, size=20, text=xxx, face='Consolas-With-Yahei')
node2 = node(x=20, y=246, size=20, text=xxx)
outputImg()
