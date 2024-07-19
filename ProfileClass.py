import numpy as np
import pickle

class Profile:

    def __init__(self, name, newDescriptor):
        self.name = name
        self.descriptor = newDescriptor
    
    def add_descriptor(self, newDescriptor):
        self.descriptor = self.compute_average(newDescriptor)

    def compute_average(self, newDescriptor):
        mean_descriptor = np.add(self.descriptor, newDescriptor)
        mean_descriptor = mean_descriptor / 2

        return mean_descriptor
