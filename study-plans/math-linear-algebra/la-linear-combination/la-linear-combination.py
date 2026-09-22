import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """
    vectors = np.array(vectors, dtype=np.float64)
    coef = np.array(coefficients, dtype=np.float64)
    comb = vectors * coef[:, None]
    return comb.sum(axis=0)