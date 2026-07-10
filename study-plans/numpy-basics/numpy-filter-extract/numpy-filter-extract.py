import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    data = np.array(data, dtype=np.float64)
    mask = data[row_start : row_stop] > threshold
    return data[row_start : row_stop][mask]