import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    concat_list = [pd.DataFrame(df) for df in dfs]
    concat_data = pd.concat(concat_list, axis=0)
    return [
        list(concat_data.shape),
        concat_data.to_dict('list')
    ]