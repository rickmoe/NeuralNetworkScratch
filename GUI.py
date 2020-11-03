from tkinter import *

class GUI:

    palette = {'blue': [64, 64, 255], 'red': [255, 0, 0], 'black': [0, 0, 0], 'white': [208, 208, 208],
               'light_gray': [192, 192, 192], 'green': [32, 192, 32], 'light_purple': [192, 128, 192],
               'orange': [255, 80, 0], 'indigo': [128, 0, 128]}

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

    def createColorsScaledLine(self, relx1, rely1, relx2, rely2, val, minVal, maxVal, color1, color2, color3=None, **kwargs):
        self.createLine(relx1, rely1, relx2, rely2, fillRGB=GUI.getColorScaleValue(val, minVal, maxVal, color1, color2, color3=color3), **kwargs)

    def runMainLoop(self):
        self.root.mainloop()

    @staticmethod
    def getColorScaleValue(val, minVal, maxVal, color1, color2, color3=None):
        if color3 is None:
            c2Weight = (val - minVal) / (maxVal - minVal)
            return GUI.blendColors(color1, color2, 1 - c2Weight, c2Weight)
        else:
            negativeOneToOne = (val - minVal) * 2 / (maxVal - minVal) - 1
            if negativeOneToOne < 0:
                return GUI.blendColors(color1, color3, abs(negativeOneToOne), 1 - abs(negativeOneToOne))
            else:
                return GUI.blendColors(color2, color3, abs(negativeOneToOne), 1 - abs(negativeOneToOne))

    @staticmethod
    def getColorScaledExponential(val, exponent, minVal, maxVal, color1, color2):
        zeroToOne = (val - minVal) / (maxVal - minVal)
        c2Weight = -pow(zeroToOne - 1, exponent) + 1
        return GUI.blendColors(color1, color2, 1 - c2Weight, c2Weight)

    @staticmethod
    def getColorScaledInfinite(val, convergenceRate, color1, color2):
        c1Weight = convergenceRate / (val + convergenceRate)
        return GUI.blendColors(color1, color2, c1Weight, 1 - c1Weight)

    @staticmethod
    def blendColors(color1, color2, c1Weight, c2Weight):
        return [int(color1[i] * c1Weight + color2[i] * c2Weight) for i in range(3)]

def rgbToHex(rgb):
    r = str(hex(rgb[0]).split('x')[1])
    g = str(hex(rgb[1]).split('x')[1])
    b = str(hex(rgb[2]).split('x')[1])
    return '#{}{}{}'.format(r.zfill(2), g.zfill(2), b.zfill(2))
