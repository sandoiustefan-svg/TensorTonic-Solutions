import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    array = np.array(x, dtype=float)
    smaller_zero = array < 0

    array[smaller_zero] = alpha * array[smaller_zero]

    return array