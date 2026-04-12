def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    output = []
    for val in values:
        angle = 2 * math.pi * val / period
        output.append([math.sin(angle), math.cos(angle)])
    return output