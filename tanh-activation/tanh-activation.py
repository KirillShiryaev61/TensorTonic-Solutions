import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    if np.isscalar(x):
        x = [x]
    X = np.asarray(x, dtype=np.float64)
    output = (np.exp(X) - np.exp(-X)) / (np.exp(X) + np.exp(-X))
    return output