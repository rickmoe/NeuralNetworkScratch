from NeuralNetManager import NeuralNetManager
from GUI import GUI

WIDTH = 600
HEIGHT = 600

layerSizes = [3, 8, 7, 4]
layerSizes2 = [8, 4, 4, 3]

nnMan = NeuralNetManager()
nnMan.createNN("NN1", layerSizes)
nnMan.createNN("NN2", layerSizes)

gui = GUI(WIDTH, HEIGHT, nnMan)