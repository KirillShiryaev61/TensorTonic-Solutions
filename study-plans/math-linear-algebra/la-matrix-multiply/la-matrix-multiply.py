import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    """
    Returns the matrix product as a float64 array.
    """
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)
    return np.dot(A, B)