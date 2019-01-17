# How to get the visual length of a text string in python
# https://stackoverflow.com/questions/32555015/how-to-get-the-visual-length-of-a-text-string-in-python

import ctypes
import cairo

class SIZE(ctypes.Structure):
    _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]


hdc = ctypes.windll.user32.GetDC(0)
size = SIZE(0, 0)

def createFontA(points, font):
    hfont = ctypes.windll.gdi32.CreateFontA(-points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
    return hfont
def selectObject(hdc, hfont):
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)
    return hfont_old

def getTextExtentPoint32A(text, size):
    ctypes.windll.gdi32.GetTextExtentPoint32W(hdc, text, len(text), ctypes.byref(size))
def selectObject(hdc, hfont_old):
    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
def deleteObject(hfont):
    ctypes.windll.gdi32.DeleteObject(hfont)
    return (size.cx, size.cy)

def GetTextDimensions(text, points, font):
    hfont = createFontA(points, font)
    hfont_old = selectObject(hdc, hfont)
    getTextExtentPoint32A(text, size)
    selectObject(hdc, hfont_old)
    return deleteObject(hfont)

for i in range(0,1200):
    for text, font in [
        ('....', 'Arial'), 
        ('WWWW', 'Arial'), 
        ('WWWW', 'Arial Narrow'),
        ('....', 'Courier New'), 
        ('WWWW', 'Courier New'), 
        ("Test", "Unknown font"),
        ('Test', 'Calibri'),
        ('你好', 'Arial Unicode MS')
        ]:
        x = GetTextDimensions(text, 12, font)

    # print('{:8} {:20} {}'.format(text, font, GetTextDimensions(text, 12, font)))