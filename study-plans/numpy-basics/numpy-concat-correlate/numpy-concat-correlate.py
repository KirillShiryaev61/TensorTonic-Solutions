import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    groups = [a, b, np.concatenate([a, b], axis=0)]
    return np.array(
        [np.corrcoef(array, rowvar=False) for array in groups]
    )