import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    v = np.array(v, dtype=np.float64)
    return np.array([
        np.linalg.norm(v, ord=1),
        np.linalg.norm(v, ord=2),
        np.linalg.norm(v, ord=np.inf)
    ])