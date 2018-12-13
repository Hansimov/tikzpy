from tikzpy import *
import tikzpy

initTikzpy('test_hello.pdf', width=600, height=500)
# arc1 = arc(x=50, y=50, r=50)
# arc2 = arc(x=150, y=90, beg=0.5*pi)
# arc2.r, arc2.end = 60, 1.9 * pi
# circ1 = circle(x=250, y=90, r=30)
# circ2 = circle(x=350, y=90, r=1)

xxx = 'π * 123 + 456 β ∬ 天地玄黄，宇宙洪荒' # 
# node1 = node(x=40, y=200, font_size=20, text=xxx)
# node2 = node(x=10, y=225, font_size=20, text=xxx, font_face='Consolas-With-Yahei')
node3 = node(c=[40,250], font_size=20, text=xxx, font_face='Source Han Sans HW SC', text_rgba=[0.5,0.0,0.0,1.0])
print(node3.c)
# node3.x = 3
# print(node3.c, node3.x, node3.y)
# node3.c = [30, 300]
# print(node3.c, node3.x, node3.y)
# node3.xy = [100, 250]
# print(node3.n)

circle(x=node3.ne[0], y=node3.ne[1], r=1)

# circ11 = circle(x=node1.x, y=node1.y, r=1)
# circ12 = circle(x=node1.x+node1.xa+node1.xb, y=node1.y+node1.ya+node1.yb, r=1)
# # circ13 = circle(x=node1.x+node1.xa+node1.xb, y=node1.y+node1.ya-node1.h, r=1)
# circ21 = circle(x=node2.x, y=node2.y, r=1)
# circ22 = circle(x=node2.x+node2.xa+node2.xb, y=node2.y+node2.ya+node2.yb, r=1)
# circ31 = circle(x=node3.x, y=node3.y, r=1)
# circ32 = circle(x=node3.x+node3.xa+node3.xb, y=node3.y+node3.ya+node3.yb, r=1)
# circ3n = circle(x=node3.n[0], y=node3.n[1], r=2)
# circ3s = circle(x=node3.s[0], y=node3.s[1], r=2)
# circ3e = circle(x=node3.e[0], y=node3.e[1], r=2)
# circ3w = circle(x=node3.w[0], y=node3.w[1], r=2)
# circ3se = circle(x=node3.se[0], y=node3.se[1], r=2)
# circ3c = circle(x=node3.c[0], y=node3.c[1], r=3)

outputImg()
