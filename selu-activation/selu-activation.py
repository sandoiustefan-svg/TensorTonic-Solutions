import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here

    array = np.array(x, dtype=float)

    bigger_zero = array > 0
    smaller_zero = array <= 0

    array[bigger_zero] = lam * array[bigger_zero]
    array[smaller_zero] = lam * alpha * (np.exp(array[smaller_zero]) - 1)

    return array
    
