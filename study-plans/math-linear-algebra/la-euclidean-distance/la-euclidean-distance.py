import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    return float(np.linalg.norm(x - y))