def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    if len(values) == 0:
        return []

    max_val = max(values)
    min_val = min(values)
    
    if max_val - min_val == 0:
        return [0] * len(values)

    weight = (max_val - min_val) / num_bins

    output = []
    for val in values:
        bins = min(int((val - min_val) / weight), num_bins - 1)
        output.append(bins)
    return output