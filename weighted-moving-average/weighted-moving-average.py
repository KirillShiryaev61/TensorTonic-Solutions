def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    output = []
    window_size = len(weights)

    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        weighted_sum = sum([window[i] * weights[i] for i in range(window_size)])
        output.append(weighted_sum / sum(weights))
    
    return output