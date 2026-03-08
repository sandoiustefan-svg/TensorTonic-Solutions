import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    array = np.array(x, dtype=float)

    less_zero = array < 0 

    array[less_zero] = 0

    return array

    