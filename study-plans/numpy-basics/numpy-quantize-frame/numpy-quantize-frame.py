import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    data = np.array(data, dtype=np.float64)
    massive = [
        np.round(data, decimals),
        np.floor(data),
        np.ceil(data)
    ]
    for i, data in enumerate(massive):
        massive[i] = np.pad(
            data, 
            pad_width=pad_width, 
            mode='constant', 
            constant_values=0
        )
    return np.stack(massive)