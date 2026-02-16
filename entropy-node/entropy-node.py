import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    length = len(y)
    if length == 0:
        return 0.0

    y = np.asarray(y)
    _, prob = np.unique(y, return_counts=True)
    prob = prob / length
    return sum(-prob * np.log2(prob))