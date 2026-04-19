import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    output = df[df[column] > threshold]
    return {
        'filtered_data': output.to_dict('list'),
        'count': output.shape[0]
    }