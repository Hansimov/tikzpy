<!-- 


=================================================
Functions
=================================================

shapes: (Indeed, all shapes are paths)
-----------------------------
    arc, circle, ellipse, ring,
    triangle, rectangle, polygon, regularpolygon
    path, line, arrow, bezier
    3d: spheres, cubes, regularpolyhedron

options(styles):
    draw, fill, shade, opacity
    decorations,
    anchor,
    linewidth (thickness)
    text
    dotted/dashed
    corner

%   It might be better to define options in each type of 


Read VisualTikZ.pdf to get more ideas.

Read SVG doc to get more ideas:
    https://www.w3.org/TR/SVG2/


node(text):
-----------------------------

options of text:
    block/text width/height, 
    inner/outer sep,
    block/text color,
    align,
    font size/face


frameworks:
-----------------------------
    tree diagram,
    * data visualization,
    timeline, flowchart, chain, cycle,
    UML,
    mindmap,
    circuits, periodic table, ...

Visit TeXample.net to get more ideas:
    http://www.texample.net/tikz/examples/all/

coordinate system
-----------------------------
    polar

include outer files
-----------------------------

LaTeX:
-----------------------------
    math formulars


style object 
-----------------------------
>   <sty> = style(<option>=<value>)
    # a 2-d list will also work ...
>   <stylist> = [['<key1>', <val1>], ['<key2>', <val2>], ...]

>   <obj>.set(<sty>)
>   <obj>.set(<stylist>)


=================================================
Grammars
=================================================
[]: options
<>: variables

xxx.setContext(cr)


>   <obj> = circle(r=<radius>,xy=[<x>,<y>])
>   <obj> = circle(r=<radis>, x=<x>, y=<y>)
>   <obj> = circle()
    <obj>.r, obj.xy = <radius>, [<x>, <y>]


# <obj>.set(<option>=<value>)

>   <obj>.set(show=True)
>   <obj>.set('show')
>   <obj>.set(['show'])
>   <obj>.show()
>   <obj>.show = True

>   <obj>.set(draw = '<color>')
>   <obj>.draw = '<color>'
>   <obj>.draw = '<color1>!<ratio>!<color2>'
>   <obj>.draw = ['rgb', [<r>, <g>, <b>]]



=================================================
Mechanisms
=================================================

Append each new object to a global list,
and display all of the (unhidden) objects in the list at last.

 -->

