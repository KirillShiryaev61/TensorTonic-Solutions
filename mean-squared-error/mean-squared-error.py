import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_true = np.array(y_true, dtype=np.float64)
    y_pred = np.array(y_pred, dtype=np.float64)

    if y_true.shape[0] != y_pred.shape[0]:
        return None

    return sum(np.power(y_pred - y_true, 2)) / y_true.shape[0]
