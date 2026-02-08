def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    output = []
    
    for value in values:
        feature = [value**power for power in range(degree+1)]
        output.append(feature)
    
    return output
