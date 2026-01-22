import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    V = np.asarray(v, dtype=np.float64)
    len_vector = np.sqrt(np.sum(V**2, axis=-1, keepdims=True))
    return V / np.maximum(len_vector, 1e-10)