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
        prevX, currY, prevY = 0, [], []
        for i in range(len(layerSizes)):
            x1 = layerWidth * (i + GUIManager.LAYER_GAP_PERCENT / 2)
            x2 = layerWidth * ((i + 1) - GUIManager.LAYER_GAP_PERCENT / 2)
            heightOffset = (max(layerSizes) - layerSizes[i]) * layerHeight / 2
            for j in range(layerSizes[i]):
                y1 = layerHeight * (j + GUIManager.NEURON_GAP_PERCENT / 2) + heightOffset
                y2 = layerHeight * ((j + 1) - GUIManager.NEURON_GAP_PERCENT / 2) + heightOffset
                currY.append((y1 + y2) / 2)
                self.gui.createOvalCorner(x1, y1, x2, y2, fillRGB=GUI.palette['green'], outlineRGB=GUI.palette['black'],
                                          text=str(round(self.neuronValueMatrix[i][j], 6)), width=2)
                for y in prevY:
                    self.gui.createLine(prevX, y, x1, (y1 + y2) / 2, fillRGB=GUI.palette['blue'], width=2)
            prevY = currY.copy()
            currY.clear()
            prevX = x2
        self.gui.runMainLoop()
