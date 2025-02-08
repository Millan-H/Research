import pandas
import numpy

class Node:
    def __init__(self, connections, weights, biases, outputs):
        self.connections=connections
        self.weights=weights
        self.biases=biases
        self.outputs=outputs
        