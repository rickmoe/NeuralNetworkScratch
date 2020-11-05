import threading
import numpy as np
from NeuralNetwork import NeuralNetwork as NN
from GUI import GUI

class GUIManager:

    LAYER_GAP_PERCENT = 0.6
    NEURON_GAP_PERCENT = 0.1

    def __init__(self):
        self.nns = {}

    def createNNGUI(self, title, width, height, layerSizes, inputVect, outputMatrix, weight3DArr, biasMatrix):
        self.nns[title]['width'] = width
        self.nns[title]['height'] = height
        self.nns[title]['gui'] = GUI(title, width, height)
        self.nns[title]['neuronValueMatrix'] = [inputVect.tolist()]
        for i in range(len(outputMatrix)):
            self.nns[title]['neuronValueMatrix'].append(outputMatrix[i].tolist())
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
                if i == len(layerSizes) - 1:
                    neuronColor = GUI.getColorScaledExponential(self.nns[title]['neuronValueMatrix'][i][j],
                                                                4, 0.0, 1.0, GUI.palette['white'], GUI.palette['orange'])
                elif i == 0:
                    neuronColor = GUI.getColorScaledExponential(self.nns[title]['neuronValueMatrix'][i][j],
                                                                2, 0.0, 1.0, GUI.palette['white'], GUI.palette['indigo'])
                else:
                    neuronColor = GUI.getColorScaledInfinite(self.nns[title]['neuronValueMatrix'][i][j],
                                                             0.06, GUI.palette['white'], GUI.palette['green'])
                self.nns[title]['gui'].createOvalCorner(x1, y1, x2, y2, fillRGB=neuronColor, outlineRGB=GUI.palette['black'],
                                          text=str(round(self.nns[title]['neuronValueMatrix'][i][j], 6)), width=1)
                for count, y in enumerate(prevY):
                    self.nns[title]['gui'].createColorsScaledLine(prevX, y, x1, (y1 + y2) / 2, weight3DArr[i - 1][j][count], -maxWeight,
                                                    maxWeight, GUI.palette['red'], GUI.palette['blue'], color3=GUI.palette['light_purple'],
                                                    width=int(abs(weight3DArr[i - 1][j][count]) * 3))
            prevY = currY.copy()
            currY.clear()
            prevX = x2
        self.nns[title]['gui'].runMainLoop()

    def createNN(self, title, width, height, layerSizes, gui=True):
        nn = NN.createRandomParameterNN(layerSizes)
        self.nns[title] = {'nn': nn}
        t = None
        if gui:
            t = threading.Thread(target=self.createNNGUI, args=[title, width, height, layerSizes, nn.getInputs(), nn.getOutputMatrix(), nn.getWeights(), nn.getBiases()])
            t.start()
        self.nns[title]['thread'] = t
