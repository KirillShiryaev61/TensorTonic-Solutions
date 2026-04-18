import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)
    dtypes_dict = {}
    for col in df.columns:
        dtypes_dict[col] = str(df[col].dtypes)
    output = {
        'rows': df.shape[0],
        'cols': df.shape[1],
        'columns': list(df.columns),
        'dtypes': dtypes_dict,
        'total_values': df.shape[0] * df.shape[1]
    }
    return output