def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    num_measure = len(points[0])
    output = [[0.0] * num_measure for _ in range(k)]
    count = [0] * k

    for i in range(len(points)):
        cls = assignments[i]
        for j in range(num_measure):
            output[cls][j] += points[i][j]
        count[cls] += 1

    for i in range(k):
        for j in range(num_measure):
            if count[i] == 0:
                continue
            output[i][j] /= count[i]
    
    return output
        