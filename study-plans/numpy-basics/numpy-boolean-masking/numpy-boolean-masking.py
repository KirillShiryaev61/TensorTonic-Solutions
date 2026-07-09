import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    data = np.array(data, dtype=np.float64)
    cond = data > threshold

    el_1 = np.where(cond, 1, 0).copy()
    el_2 = np.where(np.any(cond, axis=1)[:, np.newaxis], data, 0)
    el_3 = np.where(np.all(cond, axis=1)[:, np.newaxis], data, 0)
    return np.array([el_1, el_2, el_3])