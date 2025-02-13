from layer import Layer, LayerType

class Network:
  def __init__(self, inputLayer, hiddenLayers, outputLayer):
    self.layers = [inputLayer, *hiddenLayers, outputLayer]

  def forward(self, *inputs):
    layerInputs = list(inputs)
    for layer in self.layers:
        layerOutputs = layer.calcOutputs(layerInputs)
        # print(layerOutputs)
        layerInputs = layerOutputs
    return layerOutputs
        
