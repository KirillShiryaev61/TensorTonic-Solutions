import numpy as np

def gram_schmidt(vectors: list) -> np.ndarray:
    """
    Returns a float64 array whose rows form the ordered orthonormal basis.
    """
    Q = np.array(vectors, dtype=np.float64)
    n_rows = Q.shape[0]

    for i in range(n_rows):
        norm = np.linalg.norm(Q[i, :])
        if norm < 1e-12:
            raise ValueError(f'Вектор {i} линейно зависим')
        Q[i, :] /= norm

        for j in range(i + 1, n_rows):
            proj_coef = Q[i, :] @ Q[j, :].T
            Q[j, :] -= proj_coef * Q[i, :]
    return Q
        