import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    X = np.array(x)
    c = Counter(X)
    max_count = max(c.values())
    mode = min([item for item, values in c.items() if values == max_count])

    return (np.mean(X), np.median(X), mode)


