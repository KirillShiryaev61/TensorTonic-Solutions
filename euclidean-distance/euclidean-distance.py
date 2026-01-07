import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    X = np.array(x, dtype=np.float64)
    Y = np.array(y, dtype=np.float64)

    return np.sqrt(sum(np.power(X - Y, 2)))