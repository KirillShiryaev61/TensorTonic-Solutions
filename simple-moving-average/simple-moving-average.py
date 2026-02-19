def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    output = []
    for i in range(len(values) - window_size + 1):
        output.append(sum(values[i:i + window_size]) / window_size)
    return output
        