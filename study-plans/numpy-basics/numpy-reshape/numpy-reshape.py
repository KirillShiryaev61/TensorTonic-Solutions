import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    data = np.array(data, dtype=np.float64)
    if operation == 'flatten':
        return data.flatten()
    elif operation == 'transpose':
        return data.T
    elif operation == 'add_batch':
        return data[np.newaxis, ...]
    else:
        raise ValueError ('operation can be flatten or transpose or add_batch')
