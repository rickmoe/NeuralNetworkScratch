from NeuralNetManager import NeuralNetManager
from GUI import GUI

WIDTH = 800
HEIGHT = 800

layerSizeMatrix = [[3, 8, 7, 4], [8, 4, 4, 3], [3, 2, 2, 1], [14, 12, 11, 10], [5, 4, 3, 2, 1], [2, 3, 1], [6, 1, 1, 5], [3, 4, 6, 2], [1, 2, 2, 1], [5, 6, 7, 8]]

nnMan = NeuralNetManager()
for layerSizeList in layerSizeMatrix:
    nnMan.createNN(layerSizeList)

gui = GUI(WIDTH, HEIGHT, nnMan)
