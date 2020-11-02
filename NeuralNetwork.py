import numpy as np
from Layer import Layer

class NeuralNetwork:

    def __init__(self, layerSizes, inputVect=None, weight3DArr=None, biasMatrix=None):
        if inputVect is None:
            inputVect = []
        if weight3DArr is None:
            weight3DArr = [[[]]]
        if biasMatrix is None:
            biasMatrix = [[]]
        self.inputVect = np.array(inputVect)
        self.weight3DArr = np.array(weight3DArr, dtype=object)
        self.biasMatrix = np.array(biasMatrix, dtype=object)
        self.outputMatrix = [[]] * (len(layerSizes) - 1)
        self.outputMatrix.append(self.inputVect)
        self.outputMatrix = np.array(self.outputMatrix, dtype=object)
        self.layers = [Layer(layerSizes[i], inputVect=self.outputMatrix[i - 1], weightMatrix=weight3DArr[i], biasVect=biasMatrix[i]) for i in range(len(layerSizes))]

    def getInputs(self):
        return self.inputVect

    def setInputs(self, inVect):
        self.inputVect = np.array(inVect)

    def getWeights(self):
        return self.weight3DArr

    def setWeights(self, weight3DArr):
        self.weight3DArr = np.array(weight3DArr)

    def getBiases(self):
        return self.biasMatrix

    def setBiases(self, biasMatrix):
        self.biasMatrix = biasMatrix

    def setWeightsBias(self, weight3DArr, biasMatrix):
        self.setWeights(weight3DArr)
        self.setBiases(biasMatrix)

    def getOutputMatrix(self):
        self.calcOutput()
        return self.outputMatrix

    def getOutputs(self):
        return self.getOutputMatrix()[-1]

    def getOutput(self):
        return max(range(len(self.getOutputs())), key=self.getOutputs().__getitem__)

    def calcOutput(self):
        weightMatrix0 = np.array(self.weight3DArr[0])
        inVect = self.inputVect.T
        self.outputMatrix[0] = np.matmul(weightMatrix0, inVect) + self.biasMatrix[0]
        for i in range(1, len(self.layers)):
            self.outputMatrix[i] = np.matmul(self.weight3DArr[i], np.array(self.outputMatrix[i - 1]).T) + self.biasMatrix[i]

    @staticmethod
    def generateRandomParameters(layerSizes):
        inputVect = np.random.uniform(low=-1.0, high=1.0, size=(layerSizes[0],))
        weight3DArr = np.array([np.random.uniform(low=-1.0, high=1.0, size=(layerSizes[i],layerSizes[i-1])) for i in range(1, len(layerSizes))], dtype=object)
        biasMatrix = np.array([np.random.uniform(low=0.0, high=0.0, size=(layerSizes[i],)) for i in range(1, len(layerSizes))], dtype=object)
        return inputVect, weight3DArr, biasMatrix

    @staticmethod
    def createRandomParameterNN(layerSizes):
        layerSizes = layerSizes
        inputVect, weight3DArr, biasMatrix = NeuralNetwork.generateRandomParameters(layerSizes)
        return NeuralNetwork(layerSizes[1:], inputVect=inputVect, weight3DArr=weight3DArr, biasMatrix=biasMatrix)