import pandas as pd

def unstack_to_wide(data, index_col, columns_col, values_col):
    """
    Returns: dict with index_col plus one key per unique value in columns_col
    """
    return pd.DataFrame(data)\
             .groupby([index_col, columns_col])[values_col].sum()\
             .unstack()\
             .reset_index()\
             .to_dict('list')