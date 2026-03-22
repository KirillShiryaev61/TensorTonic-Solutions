def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    output = []
    calc_value = int(window_size / 2 + 0.5) - 1

    for point in range(len(values) - window_size + 1):
        window = sorted(values[point:point + window_size])
        if window_size % 2 == 1:
            output.append(window[calc_value])
        else:
            mean_value = (window[calc_value] + window[calc_value + 1]) / 2
            output.append(mean_value)
    return output