import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x, dtype=torch.float32)
    if op == 'flatten':
        result = x.flatten()
    elif op == 'squeeze':
        result = x.squeeze()
    elif op == 'transpose':
        result = x.permute(1, 0)
    else:
        ValueError('Unknown op')
    return result.tolist()
