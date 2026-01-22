import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    X = np.asarray(x, dtype=np.float64)
    return np.where(X < 0, X * alpha, X)