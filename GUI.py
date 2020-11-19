import numpy as np
from tkinter import *

class GUI:

    palette = {'blue': [64, 64, 255], 'red': [255, 0, 0], 'black': [0, 0, 0], 'white': [208, 208, 208],
               'light_gray': [192, 192, 192], 'green': [32, 192, 32], 'light_purple': [192, 128, 192],
               'orange': [255, 80, 0], 'indigo': [128, 0, 128]}
    ENTRY_SIZE = 20
    LAYER_GAP_PERCENT = 0.6
    NEURON_GAP_PERCENT = 0.1

    def __init__(self, width, height, nnMan):
        self.height = height
        self.width = width
        self.nnMan = nnMan
        self.root = Tk()
        self.root.resizable(False, False)
        self.canvas = Canvas(self.root, height=height + self.ENTRY_SIZE, width=width, bg=rgbToHex(GUI.palette['light_gray']))
        self.canvas.pack()
        self.currNNIndex = 0
        self.setCurrNN(self.currNNIndex)

    def drawNNGUI(self, layerSizes, inputVect, outputMatrix, weight3DArr, biasMatrix):
        self.canvas.delete("all")
        self.root.title(self.getCurrNN().getTitle())
        self.valueMatrix = [list(inputVect)]
        for i in range(len(outputMatrix)):
           self.valueMatrix.append(outputMatrix[i].tolist())
        layerWidth = (1 / len(layerSizes))
        layerHeight = (1 / max(layerSizes))
        maxWeight = abs(max([max([max([weight3DArr[i][j][k] for k in range(len(weight3DArr[i][j]))], key=abs)
                                  for j in range(len(weight3DArr[i]))], key=abs)
                             for i in range(len(weight3DArr))], key=abs))
        prevX, currY, prevY = 0, [], []
        for i in range(len(layerSizes)):
            x1 = layerWidth * (i + self.LAYER_GAP_PERCENT / 2)
            x2 = layerWidth * ((i + 1) - self.LAYER_GAP_PERCENT / 2)
            heightOffset = (max(layerSizes) - layerSizes[i]) * layerHeight / 2
            for j in range(layerSizes[i]):
                y1 = layerHeight * (j + self.NEURON_GAP_PERCENT / 2) + heightOffset
                y2 = layerHeight * ((j + 1) - self.NEURON_GAP_PERCENT / 2) + heightOffset
                currY.append((y1 + y2) / 2)
                if i == len(layerSizes) - 1:
                    neuronColor = self.getColorScaledExponential(self.valueMatrix[i][j], 4, 0.0, 1.0, GUI.palette['white'], GUI.palette['orange'])
                elif i == 0:
                    neuronColor = self.getColorScaledExponential(self.valueMatrix[i][j], 2, 0.0, 1.0, GUI.palette['white'], GUI.palette['indigo'])
                else:
                    neuronColor = self.getColorScaledInfinite(self.valueMatrix[i][j], 0.06, GUI.palette['white'], GUI.palette['green'])
                self.createOvalCorner(x1, y1, x2, y2, fillRGB=neuronColor, outlineRGB=GUI.palette['black'], text=str(round(self.valueMatrix[i][j], 6)), width=1)
                for count, y in enumerate(prevY):
                    self.createColorsScaledLine(prevX, y, x1, (y1 + y2) / 2, weight3DArr[i - 1][j][count], -maxWeight, maxWeight,
                                                GUI.palette['red'], GUI.palette['blue'], color3=GUI.palette['light_purple'],
                                                width=int(abs(weight3DArr[i - 1][j][count]) * 3))
            prevY = currY.copy()
            currY.clear()
            prevX = x2
        self.createCommandBox()
        self.runMainLoop()

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

    def createCommandBox(self):
        self.cmdTxt = StringVar()
        self.cmdBox = Entry(self.root, bg=rgbToHex(GUI.palette['white']), width=100, textvariable=self.cmdTxt)
        self.cmdBox.place(x=0, y=self.height)
        self.root.bind('<Return>', self.checkCommand)
        self.cmdBox.focus()

    def createColorsScaledLine(self, relx1, rely1, relx2, rely2, val, minVal, maxVal, color1, color2, color3=None, **kwargs):
        self.createLine(relx1, rely1, relx2, rely2, fillRGB=GUI.getColorScaleValue(val, minVal, maxVal, color1, color2, color3=color3), **kwargs)

    def runMainLoop(self):
        self.root.mainloop()

    def checkCommand(self, event):
        cmd = self.cmdBox.get()
        if cmd.startswith('d'):
            nums = [int(i) for i in cmd.split() if i.isdigit()]
            if len(nums) > 0:
                try:
                    self.setCurrNN(nums[0])
                except:
                    print("Can't change display")
        elif cmd.startswith('i'):
            nums = [float(i) for i in cmd.split() if i[0].isdigit()]
            if len(nums) > 1:
                try:
                    self.nnMan.getNNs()[self.currNNIndex].setInput(int(nums[0]), nums[1])
                except:
                    print("Can't set input")
                self.setCurrNN(self.currNNIndex)
        elif 'q' is cmd:
            self.root.destroy()
        self.cmdTxt.set("")

    def setCurrNN(self, nnIndex):
        self.currNNIndex = nnIndex
        nn = self.getCurrNN()
        self.drawNNGUI(nn.layerSizes, nn.getInputs(), nn.getOutputMatrix(), nn.getWeights(), nn.getBiases())

    def getCurrNN(self):
        return self.nnMan.getNNs()[self.currNNIndex]

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
