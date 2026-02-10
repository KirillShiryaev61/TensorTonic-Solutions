def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    output = []

    for p in points:
        best_dist = float('inf')
        best_idx = None
        for idx, c in enumerate(centroids):
            distance = sum((p[i] - c[i])**2 for i in range(len(p)))
            if distance < best_dist:
                best_dist = distance
                best_idx = idx
        output.append(best_idx)

    return output