from tikzpy import *
import tikzpy

initTikzpy('test_hello.pdf', width=600, height=1500)
# arc1 = arc(x=50, y=50, r=50)
# arc2 = arc(x=150, y=90, beg=0.5*pi)
# arc2.r, arc2.end = 60, 1.9 * pi
# circ1 = circle(x=250, y=90, r=30)
# circ2 = circle(x=350, y=90, r=1)

xxx = 'π * 123 + 456 β ∬ 天地玄黄，宇宙洪荒' # 
# node1 = node(x=00, y=200, font_size=20, text=xxx, anchor='l')
# node2 = node(x=10, y=225, font_size=20, text=xxx, font_face='Consolas-With-Yahei')
node3 = node(anchor='l', x=20, y=250, font_size=20, text=xxx, font_face='Source Han Sans HW SC', text_rgba=[0.5,0.0,0.0,1.0])
# node3.anchor = 'l'
node3.is_stroke = True
# circle(x=node3.e[0], y=node3.e[1], r=1)

# node3.e = [400, 250]
node3.text = 'π * 123 + abc β ∬ 日月盈昃'
print(node3.l)
node3.anchor = 'sw'
print(node3.c)
print(node3.asepl)
print(node3.asepe)
node3.asept = 10
print(node3.asep)
node3.asep[1] = 10

circle(x=node3.e[0], y=node3.e[1], r=2)
circle(x=node3.n[0], y=node3.n[1], r=2)
circle(x=node3.l[0], y=node3.l[1], r=2)
circle(x=node3.b[0], y=node3.b[1], r=2)

# node_list = []
# for i in range(0, 1000):
#     yyy = str(i)
#     cox = 50 + 20 *(i % 20)
#     coy = 50+ 20 * int(i/20)
#     node_list.append(node(font_size=10, text='', font_face='Source Han Sans HW SC', x=cox, y=coy, anchor='c', text_rgba=[0.5,0.0,0.0,1.0]))
#     # node_list[i].anchor = 'n'
#     node_list.append(circle(x=cox, y=coy, r=10))

outputImg()
