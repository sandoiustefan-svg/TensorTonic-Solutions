import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here

    array = np.array(x, dtype=float)
    less_zero = array < 0

    array[less_zero] = alpha * (np.exp(array[less_zero]) - 1)
        
    return array.tolist() 