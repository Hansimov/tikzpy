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
    # print(ELEMENTS)

    # This line below finishes the Surface and drops all references to external resources.
    # Without this, the output file will be busy and other programs could not use it (like gswin64c) in os.system().
    #   https://pycairo.readthedocs.io/en/latest/reference/surfaces.html#cairo.Surface.finish
    PDF_SURFACE.finish()
