def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    output = []
    t = max(lags)

    for i in range(t, len(series)):
        row = [series[i - j] for j in lags]
        output.append(row)

    return output
    
    
    
    