import os

def compileTex(cp_type='xelatex'):
    if cp_type == 'xelatex' or cp_type == 'x':
        compile_type = '-xelatex'
    else:
        compile_type = '-pdf'

    compile_tool = 'latexmk -pv '+ compile_type + ' '
    absolute_tex_filename = os.path.join(os.getcwd(), tex_filename)
    os.system(compile_tool + absolute_tex_filename)

def clearTex():
    with open(tex_filename, 'w'):
        pass

def beginDoc(doctype='standalone'):
    if doctype == 'article' or doctype == 'a':
        doccls_cmd = '\\documentclass{article}\n'
    else:
        doccls_cmd = '\\documentclass[tikz]{standalone}\n'

    printTex(doccls_cmd)

    begin_doc_list = [
        '\\input{tikz-common-settings}\n',
        '\\begin{document}\n'
    ]

    printTex(begin_doc_list)

    return doctype

def endDoc():
    end_doc_list = [
        '\n\\end{document}'
    ]
    printTex(end_doc_list)

def beginTikz():
    begin_tikz_list = [
        '\\begin{tikzpicture}\n'
    ]
    printTex(begin_tikz_list)

def endTikz():
    end_tikz_list = [
        '\n\\end{tikzpicture}\n'
    ]
    printTex(end_tikz_list)

def printTex(commands):
    with open(tex_filename, 'a') as txf:
        if isinstance(commands, str):
            print(commands, file=txf)
        elif isinstance(commands, list):
            for line in commands:
                print(line, file=txf)

'''
class:
    - Format 1: path, draw, node
    - Format 2: grid(point1, point2).draw()
    > necessary and optional
    > primitives and addons
    > methods and properties:
        linepos, linecnt
monitor:
    interfiles
    record info of nodes and paths: linepos, linecnt, options
    only records those have returned objects?
    update linepos, linecnt when one command changes
parser/translator:
    change command and options to TikZ command
config/preamble:
    packages, pagesize
return:
    an object,
    whose properties can be updated by interfile and parser
'''

if __name__ == '__main__':
    tex_filename = 'tikzpy-hello.tex'

    clearTex()
    beginDoc()
    for i in range(0, 3601):
        beginTikz()
        cmd_list = [
            '\\draw[step=.5cm,gray,very thin] (-1.4,-1.4) grid (1.4,1.4);',
            '\\draw (-1.5,0) -- (1.5,0);',
            '\\draw (0,-1.5) -- (0,1.5);',
            '\\draw (0,0) circle [radius=1cm];',
            '\\draw (3mm,0mm) arc [start angle=0, end angle={}, radius=3mm];'.format(i*0.1)
        ]

        printTex(cmd_list)
        endTikz()
    endDoc()
    compileTex()
