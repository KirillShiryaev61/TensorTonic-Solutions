def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    output = []
    for i in range(1, len(series)):
        if series[i - 1] == 0:
            output.append(0.0)
        else:
            prc = (series[i] - series[i - 1]) / series[i - 1]
            output.append(prc)

    return output