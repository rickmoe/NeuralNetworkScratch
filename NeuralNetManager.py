from NeuralNetFramework.NeuralNetwork import NeuralNetwork as NN

class NeuralNetManager:

    def __init__(self):
        self.nns = []

    def createNN(self, layerSizes):
        nn = NN.createRandomParameterNN(layerSizes)
        self.nns.append(nn)

    def getNNs(self):
        return self.nns
