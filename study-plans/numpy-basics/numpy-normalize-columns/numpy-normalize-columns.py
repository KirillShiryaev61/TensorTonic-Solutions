import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    data = np.array(data, dtype=np.float64)
    return (data - data.mean(axis=0)) / np.maximum(data.std(axis=0), 1e-7)