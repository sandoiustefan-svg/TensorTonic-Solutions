import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x, dtype=float)

    if x.ndim == 1:
        x = x - np.max(x)
        exp_x = np.exp(x)
        softmax = exp_x / np.sum(exp_x)
        return softmax.tolist()

    x = x - np.max(x, axis=1, keepdims=True)
    exp_x = np.exp(x)
    softmax = exp_x / np.sum(exp_x, axis=1, keepdims=True)

    return softmax.tolist()