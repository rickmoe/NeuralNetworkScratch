import numpy as np
from NeuralNetwork import NeuralNetwork as NN
from GUIManager import GUIManager

HEIGHT = 800
WIDTH = 800

# inputVect = [1, 2, 3]
# weight3DArr = [[[0.5, 0.7, 0.5],
#                 [0.5, 0.2, 0.4],
#                 [1, 2.1, 15],
#                 [8, 0.3, 12]],
#                [[1, 1, 1, 1],
#                 [2, 2, 2, 2]]]
# biasMatrix = [[2, 1, 4, 3],
#               [0, 1]]
# layerSizes = [len(biasVect) for biasVect in biasMatrix]

layerSizes = [3, 8, 6, 4]
nn = NN.createRandomParameterNN(layerSizes)
guiManager = GUIManager(WIDTH, HEIGHT, layerSizes, nn.getInputs(), nn.getOutputMatrix(), nn.getWeights(), nn.getBiases())
# print(nn.getOutputMatrix())
# print()
# print(nn.getOutputs())
# print(nn.getOutput())
