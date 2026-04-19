import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    series = pd.DataFrame(data)[column].tolist()
    return {
        'values': series,
        'length': len(series)
    }