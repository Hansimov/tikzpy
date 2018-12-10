import os
import cairo

PDF_SURFACE = []
CONTEXT = []
ELEMENTS = []

def initTikzpy(filename='default.pdf', width=1280, height=720):
    global PDF_SURFACE, CONTEXT
    PDF_SURFACE = cairo.PDFSurface(filename, width, height)
    CONTEXT = cairo.Context(PDF_SURFACE)
    # print(CONTEXT)

def outputImg():
    print('ELEMENTS SIZE: {}'.format(len(ELEMENTS)))
    for ele in ELEMENTS:
        CONTEXT.save()
        ele.paint()
        CONTEXT.restore()
