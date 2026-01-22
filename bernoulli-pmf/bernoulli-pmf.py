import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    X = np.asarray(x)
    X = np.where(X == 1, p, 1 - p)
    return (X, p, p * (1 - p))