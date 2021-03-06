import numpy as np
from NeuralNetFramework.Layer import Layer

class NeuralNetwork:

    DEFAULT_NAMES = 0

    def __init__(self, layerSizes, inputVect, weight3DArr, biasMatrix, title=None):
        if title == None:
            title = 'Neural Network #{}'.format(NeuralNetwork.DEFAULT_NAMES)
        if 'Neural Network #' in title:
            NeuralNetwork.DEFAULT_NAMES += 1
        self.title = title
        self.layerSizes = [len(inputVect)] + layerSizes
        self.inputVect = np.array(inputVect)
        self.weight3DArr = np.array(weight3DArr, dtype=object)
        self.biasMatrix = np.array(biasMatrix, dtype=object)
        self.outputMatrix = [[]] * (len(layerSizes) - 1)
        self.outputMatrix.append(self.inputVect)
        self.outputMatrix = np.array(self.outputMatrix, dtype=object)
        self.layers = [Layer(layerSizes[i], inputVect=self.outputMatrix[i - 1], weightMatrix=weight3DArr[i], biasVect=biasMatrix[i]) for i in range(len(layerSizes))]

    def getTitle(self):
        return self.title

    def getLayerSizes(self):
        return self.layerSizes

    def getInputs(self):
        return self.inputVect

    def setInputs(self, inVect):
        self.inputVect = np.array(inVect)

    def setInput(self, index, val):
        self.inputVect[index] = val

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
        NeuralNetwork.hiddenLayerActivationFunction(self.outputMatrix[0])
        for i in range(1, len(self.layers)):
            self.outputMatrix[i] = np.matmul(self.weight3DArr[i], np.array(self.outputMatrix[i - 1]).T) + self.biasMatrix[i]
            if i < len(self.layers) - 1:
                NeuralNetwork.hiddenLayerActivationFunction(self.outputMatrix[i])
            else:
                self.outputMatrix[i] = NeuralNetwork.outputLayerActivationFunction(self.outputMatrix[i])

    @staticmethod
    def hiddenLayerActivationFunction(layerVals):     # Rectified Linear
        for i in range(len(layerVals)):
            layerVals[i] = max(layerVals[i], 0)

    @staticmethod
    def outputLayerActivationFunction(layerVals):     # Softmax
        e_layerVals = np.exp(layerVals - np.max(layerVals))
        return e_layerVals / e_layerVals.sum()

    @staticmethod
    def generateRandomParameters(layerSizes):
        inputVect = np.random.uniform(low=0.0, high=1.0, size=(layerSizes[0],))
        weight3DArr = np.array([np.random.uniform(low=-1.0, high=1.0, size=(layerSizes[i], layerSizes[i-1])) for i in range(1, len(layerSizes))], dtype=object)
        biasMatrix = np.array([np.random.uniform(low=-1.0, high=1.0, size=(layerSizes[i],)) for i in range(1, len(layerSizes))], dtype=object)
        return inputVect, weight3DArr, biasMatrix

    @staticmethod
    def createRandomParameterNN(layerSizes):
        inputVect, weight3DArr, biasMatrix = NeuralNetwork.generateRandomParameters(layerSizes)
        return NeuralNetwork(layerSizes[1:], inputVect=inputVect, weight3DArr=weight3DArr, biasMatrix=biasMatrix)
