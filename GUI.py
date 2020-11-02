from tkinter import *

class GUI:

    palette = {'blue': [64, 64, 255], 'red': [255, 48, 48], 'black': [0, 0, 0], 'white': [255, 255, 255],
               'light_gray': [192, 192, 192], 'green': [32, 192, 32]}

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.root = Tk()
        self.root.title("Neural Net Visualizer")
        self.root.resizable(False, False)

        self.canvas = Canvas(self.root, height=height, width=width, bg=rgbToHex(GUI.palette['light_gray']))
        self.canvas.pack()

    def createOvalCenter(self, relx, rely, relRx, relRy, fillRGB=None, outlineRGB=None, text="", **kwargs):
        relx *= self.width
        rely *= self.height
        relRx *= self.width
        relRy *= self.height
        self.canvas.create_oval(relx-relRx, rely-relRy, relx+relRx, rely+relRy, fill=rgbToHex(fillRGB), outline=rgbToHex(outlineRGB), **kwargs)
        self.canvas.create_text(relx, rely, text=text, fill=rgbToHex(GUI.palette['black']))

    def createOvalCorner(self, relx1, rely1, relx2, rely2, fillRGB=None, outlineRGB=None, text="", **kwargs):
        relx1 *= self.width
        rely1 *= self.height
        relx2 *= self.width
        rely2 *= self.height
        self.canvas.create_oval(relx1, rely1, relx2, rely2, fill=rgbToHex(fillRGB), outline=rgbToHex(outlineRGB), **kwargs)
        self.canvas.create_text(int((relx1 + relx2) / 2), int((rely1 + rely2) / 2), text=text, fill=rgbToHex(GUI.palette['black']))

    def createLine(self, relx1, rely1, relx2, rely2, fillRGB=None, **kwargs):
        relx1 *= self.width
        rely1 *= self.height
        relx2 *= self.width
        rely2 *= self.height
        self.canvas.create_line(relx1, rely1, relx2, rely2, fill=rgbToHex(fillRGB), **kwargs)

    def runMainLoop(self):
        self.root.mainloop()

def rgbToHex(rgb):
    r = str(hex(rgb[0]).split('x')[1])
    g = str(hex(rgb[1]).split('x')[1])
    b = str(hex(rgb[2]).split('x')[1])
    return '#{}{}{}'.format(r.zfill(2), g.zfill(2), b.zfill(2))
