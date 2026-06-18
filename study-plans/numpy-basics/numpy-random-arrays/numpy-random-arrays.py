import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    np.random.seed(seed)
    if kind == 'uniform':
        return np.random.rand(shape[0], shape[1])
    elif kind == 'normal':
        return np.random.randn(shape[0], shape[1])
    else:
        raise ValueError ('kind can only be uniform or normal')