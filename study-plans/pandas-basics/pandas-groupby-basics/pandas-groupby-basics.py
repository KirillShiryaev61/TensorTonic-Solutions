import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data)
    group = df.groupby(group_col)[value_col].agg(['sum', 'mean', 'count'])
    return {
        'sum': group['sum'].to_dict(),
        'mean': group['mean'].to_dict(),
        'count': group['count'].to_dict()
    }