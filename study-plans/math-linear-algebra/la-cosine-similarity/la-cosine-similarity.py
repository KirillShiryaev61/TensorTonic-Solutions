import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    cos_sim = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return float(np.nan_to_num(cos_sim, nan=0.0))