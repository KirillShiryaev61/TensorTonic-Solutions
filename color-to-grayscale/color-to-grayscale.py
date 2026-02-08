def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    output = []

    for i in range(len(image)):
        row = []
        for j in range(len(image[i])):
            r = 0.299 * image[i][j][0]
            g = 0.587 * image[i][j][1]
            b = 0.114 * image[i][j][2]
            row.append(r + g + b)
        output.append(row)

    return output