from GUIManager import GUIManager

HEIGHT = 600
WIDTH = 600

layerSizes = [3, 8, 7, 4]
layerSizes2 = [8, 4, 4, 3]

gm = GUIManager()
gm.createNN("NN1", WIDTH, HEIGHT, layerSizes, gui=True)
gm.createNN("NN2", WIDTH, HEIGHT, layerSizes2, gui=True)
