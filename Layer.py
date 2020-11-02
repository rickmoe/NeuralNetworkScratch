import numpy as np
from Neuron import Neuron

class Layer:

    def __init__(self, size, inputVect=None, weightMatrix=None, biasVect=None):
        if inputVect is None:
            inputVect = []
        if weightMatrix is None:
            weightMatrix = [[]]
        if biasVect is None:
            biasVect = []
        self.inputVect = np.array(inputVect)
        self.weightMatrix = np.array(weightMatrix)
        self.biasVect = np.array(biasVect)
        self.outputVect = np.array([])
        self.neurons = [Neuron(self.inputVect) for _ in range(size)]

    def getInputs(self):
        return self.inputVect

    def setInputs(self, inVect):
        self.inputVect = np.array(inVect)

    def getWeights(self):
        return self.weightMatrix

    def setWeights(self, weightMatrix):
        self.weightMatrix = np.array(weightMatrix)

    def getBiases(self):
        return self.biasVect

    def setBiases(self, biasVect):
        self.biasVect = biasVect

    def setWeightsBias(self, weightMatrix, biasVect):
        self.setWeights(weightMatrix)
        self.setBiases(biasVect)

    def getOutput(self):
        self.calcOutput()
        return self.outputVect

    def calcOutput(self):
        self.outputVect = np.matmul(self.weightMatrix, self.inputVect.T) + self.biasVect
