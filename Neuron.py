import numpy as np

class Neuron:

    def __init__(self, inVect=None, weightVect=None, bias=0):
        if inVect is None:
            inVect = []
        if weightVect is None:
            weightVect = []
        self.inputVect = np.array(inVect)
        self.weightVect = np.array(weightVect)
        self.bias = np.array(bias)
        self.output = np.array(0)

    def getInputs(self):
        return self.inputVect

    def setInputs(self, inVect):
        self.inputVect = np.array(inVect)

    def getWeights(self):
        return self.weightVect

    def setWeights(self, weightVect):
        self.weightVect = np.array(weightVect)

    def getBias(self):
        return self.bias

    def setBias(self, bias):
        self.bias = bias

    def setWeightsBias(self, weightVect, bias):
        self.setWeights(weightVect)
        self.setBias(bias)

    def getOutput(self):
        self.calcOutput()
        return self.output

    def calcOutput(self):
        self.output = np.dot(self.inputVect, self.weightVect) + self.bias
