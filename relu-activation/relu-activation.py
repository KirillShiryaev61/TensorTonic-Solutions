import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    if np.isscalar(x):
        x = [x]
    return np.maximum(x, 0)