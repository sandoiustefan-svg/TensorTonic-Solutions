import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    array = np.array(x)

    tanh = (np.exp(array) - np.exp(-array)) / (np.exp(array) + np.exp(-array))

    return tanh