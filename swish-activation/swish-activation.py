import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    array = np.array(x, dtype=float)

    swish = array * (1 / (1 + np.exp(-array)))

    return swish