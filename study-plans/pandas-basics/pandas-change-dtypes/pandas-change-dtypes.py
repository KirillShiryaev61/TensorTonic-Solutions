import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    df = pd.DataFrame(data)
    dtypes_before = {}
    dtypes_after = {}
    
    for col in df.columns:
        dtypes_before[col] = str(df[col].dtype)

    df[column] = df[column].astype(target_type)

    for col in df.columns:
        dtypes_after[col] = str(df[col].dtype)

    return [dtypes_before, dtypes_after]
        