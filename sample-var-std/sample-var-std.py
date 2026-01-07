import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    X = np.array(x, dtype=np.float64)
    var = sum(np.power(X - np.mean(X), 2)) / (X.shape[0] - 1)
    
    return (var, np.sqrt(var))