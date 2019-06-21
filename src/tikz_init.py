import os
import cairo

PDF_SURFACE = []
CONTEXT = []
ELEMENTS = []

def initTikzpy(filename='tikzpy.pdf', width=1280, height=720):
    global PDF_SURFACE, CONTEXT, ELEMENTS
    PDF_SURFACE = cairo.PDFSurface(filename, width, height)
    CONTEXT = cairo.Context(PDF_SURFACE)
    # Clear current surface, if there are more than one surface
    # ELEMENTS = []
    # print(CONTEXT)

def outputImg():
    print('ELEMENTS NUM: {}'.format(len(ELEMENTS)))
    for ele in ELEMENTS:
        ele.paint()
        # print(type(ele))
    # PDF_SURFACE.write_to_png('z_test_hello.png')
    print(ELEMENTS)
