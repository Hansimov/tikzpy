from tikzpy import *
# import tikzpy
from random import randint

initTikzpy('z_test_hello.pdf', width=1280, height=720)
# arc1 = arc(x=50, y=50, r=50)
# arc2 = arc(x=150, y=90, beg=0.5*pi)
# arc2.r, arc2.end = 60, 1.9 * pi
# circ1 = circle(x=250, y=90, r=30)
# circ2 = circle(x=350, y=90, r=1)

xxx = u'π * 123 + 45678 β ∬ Σ \n天地玄黄，宇宙洪荒。日月盈昃，辰宿列张。\n寒来暑往，秋收冬藏。闰余成岁，律吕调阳。\n云腾致雨，露结为霜。金生丽水，玉出昆冈。\n剑号巨阙，珠称夜光。果珍李柰，菜重芥姜。\n\u27bd\n'
box1 = node(xy=[250, 200], font_size=15, max_width=805, min_width=420, text=xxx, line_space=5, anchor='c', is_stroke=True,is_fill=False, align='r')
box1.font_size = 16
# print(node1.c)
# box1 = node(xy=[300, 150], font_size=10, anchor='l', is_stroke=True, font_face='CMU Typewritter Text',  text='π * 123 + 45678 β ∬ Σ ')
# print(box1.c, box1.l)
# box1.c = [200,100]
circle(xy=getattr(box1, box1.anchor))
# print(box1.c, box1.l)
# print(box1.wh)
# box1.se = [100,100]
# print(box1.c, box1.l)

# circle(c=[300,200])
# node1.calcWH()
# box1 = box(anchor='bl', text='123414', xy=[300, 200], font_size=10, )
# box1.updateWH()
# box1.anchor = 'bl'
# print(box1.wh, box1.xy, box1.c)
# print(box1.width)
# print(box1.text)
# node2 = node(x=10, y=225, font_size=20, text=xxx, font_face='Consolas-With-Yahei')
# node3 = node(anchor='l', x=20, y=250, font_size=20, text=xxx, font_face='Source Han Sans HW SC', text_rgba=[0.5,0.0,0.0,1.0])
# node3.font_face = 'Arial Unicode MS'
# node3.anchor = 'l'
# node3.is_stroke = True
# circle(c=node3.e, r=2)

# node3.e = [400, 250]
# node3.text = 'π * 123 + abc β ∬ 日月盈昃'
# print(node3.l)
# node3.anchor = 'sw'
# print(node3.c)
# print(node3.asepl)
# print(node3.asepe)
# node3.asept = 10
# print(node3.asep)
# node3.asep[1] = 10

# circle(x=node3.e[0], y=node3.e[1], r=2)
# circle(x=node3.n[0], y=node3.n[1], r=2)
# circle(x=node3.l[0], y=node3.l[1], r=2)
# print(type(circle(x=node3.b[0], y=node3.b[1], r=2)))

# box_list = []
# NUM = 1
# STEP = sqrt(NUM)
# for i in range(0, NUM):
#     yyy = str(i)
#     cox = 50 + 10 *(i % STEP) + randint(1,10)
#     coy = 50 + 10 * int(i/STEP) + randint(1,5)
    # node_list.append(node(font_size=10, text='', font_face='Source Han Sans HW SC', x=cox, y=coy, anchor='c', text_rgba=[0.5,0.0,0.0,1.0]))
    # node_list[i].anchor = 'n'
    # node_list.append(circle(c=[cox,coy], r=2))
    # box_list.append(box(text='你好', font_size=4, font_face='Arial Unicode MS', xy=[cox,coy], is_stroke=False))
    # newPage()


# point_list = [[100,50], [100,80], [200,20], [250,90], [320, 30], [400,100]]
# for point in point_list:
#     circle(c=point, r=3)

# line1 = line(points=point_list)
# line1.is_smooth = True
# line1.is_dot = True
# line1.smoothness = 0.25

# print(line1.points[0], line1.points[-1])
# line2 = line(points=point_list, stroke_rgba=[1.0,0,0,1.0])
# line1.tip.len = 15
# line1.tip.angle = 1.4*pi
# line1.tip.ratio = 0.3
# line1.tip.is_fill = False

outputImg()

