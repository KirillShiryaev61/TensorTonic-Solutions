def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    for _ in range(order):
        temp = []
        for i in range(1, len(series)):
            diff = series[i] - series[i - 1]
            temp.append(diff)
        series = temp

    return series