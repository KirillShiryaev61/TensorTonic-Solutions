def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    ema = [values[0]]
    for i, value in enumerate(values[1:]):
        ema_value = alpha * value + (1 - alpha) * ema[i]
        ema.append(ema_value)
    return ema
    