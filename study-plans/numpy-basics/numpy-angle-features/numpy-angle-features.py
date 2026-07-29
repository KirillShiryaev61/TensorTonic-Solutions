import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    angels = np.degrees(angles)
    return np.array(
        [
            np.sin(angles),
            np.cos(angles),
            np.tan(angles)
        ], dtype=np.float64
    )