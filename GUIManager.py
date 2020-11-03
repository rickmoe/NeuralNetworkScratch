import numpy as np
from tkinter import LAST
from GUI import GUI

class GUIManager:

    LAYER_GAP_PERCENT = 0.6
    NEURON_GAP_PERCENT = 0.1

    def __init__(self, width, height, layerSizes, inputVect, outputMatrix, weight3DArr, biasMatrix):
        self.width = width
        self.height = height
        self.gui = GUI(self.width, self.height)
        self.neuronValueMatrix = [inputVect.tolist()]
        for i in range(len(outputMatrix)):
            self.neuronValueMatrix.append(outputMatrix[i].tolist())
        layerWidth = (1 / len(layerSizes))
        layerHeight = (1 / max(layerSizes))
        maxWeight = abs(max([max([max([weight3DArr[i][j][k] for k in range(len(weight3DArr[i][j]))], key=abs)
                                  for j in range(len(weight3DArr[i]))], key=abs)
                             for i in range(len(weight3DArr))], key=abs))
        prevX, currY, prevY = 0, [], []
        for i in range(len(layerSizes)):
            x1 = layerWidth * (i + GUIManager.LAYER_GAP_PERCENT / 2)
            x2 = layerWidth * ((i + 1) - GUIManager.LAYER_GAP_PERCENT / 2)
            heightOffset = (max(layerSizes) - layerSizes[i]) * layerHeight / 2
            for j in range(layerSizes[i]):
                y1 = layerHeight * (j + GUIManager.NEURON_GAP_PERCENT / 2) + heightOffset
                y2 = layerHeight * ((j + 1) - GUIManager.NEURON_GAP_PERCENT / 2) + heightOffset
                currY.append((y1 + y2) / 2)
                if i < len(layerSizes) - 1:
                    neuronColor = GUI.getColorScaledInfinite(self.neuronValueMatrix[i][j], 0.06, GUI.palette['white'], GUI.palette['green'])
                else:
                    neuronColor = GUI.getColorScaledExponential(self.neuronValueMatrix[i][j], 4, 0.0, 1.0, GUI.palette['white'], GUI.palette['orange'])
                self.gui.createOvalCorner(x1, y1, x2, y2, fillRGB=neuronColor, outlineRGB=GUI.palette['black'],
                                          text=str(round(self.neuronValueMatrix[i][j], 6)), width=1)
                for count, y in enumerate(prevY):
                    # self.gui.createLine(prevX, y, x1, (y1 + y2) / 2, fillRGB=GUI.palette['blue'], width=2)
                    self.gui.createColorsScaledLine(prevX, y, x1, (y1 + y2) / 2, weight3DArr[i - 1][j][count], -maxWeight,
                                                    maxWeight, GUI.palette['red'], GUI.palette['blue'], color3=GUI.palette['light_purple'],
                                                    width=int(abs(weight3DArr[i - 1][j][count]) * 3))
            prevY = currY.copy()
            currY.clear()
            prevX = x2
        self.gui.runMainLoop()
        # print(self.gui.getColorScaleValue(0, -10, 10, GUI.palette['red'], GUI.palette['blue']))
