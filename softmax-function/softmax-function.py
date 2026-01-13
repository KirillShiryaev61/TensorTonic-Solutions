import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    X = np.asarray(x, dtype=np.float64)
    
    if X.ndim == 2:
        axis = 1
    else:
        axis = None

    maximum = np.max(X, axis=axis, keepdims=True)
    
    return (np.exp(X - maximum) / 
            np.sum(np.exp(X - maximum), axis=axis, keepdims=True))