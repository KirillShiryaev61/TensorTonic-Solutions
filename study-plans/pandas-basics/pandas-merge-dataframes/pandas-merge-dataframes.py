import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    df_left = pd.DataFrame(left)
    df_right = pd.DataFrame(right)
    return df_left.merge(df_right, 
                         how=how,
                         on=on)\
                  .to_dict('list')