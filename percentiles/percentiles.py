import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    X = np.sort(np.array(x, dtype=np.float64))
    percentiles = list(q)
    output = []
    
    for perc in percentiles: 
        output.append(np.percentile(X, perc))

    return np.array(output, dtype=np.float64)
        

        
        



    
    