import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype=torch.float32)

    if method == 'relu':
        result = torch.clamp(x, min=0)
    elif method == 'sigmoid':
        result = 1 / (1 + torch.exp(-x))
    elif method == 'tanh':
        result = torch.tanh(x)
    elif method == 'leaky_relu':
        result = torch.where(x > 0, x, x * 0.01)
    else:
        ValueError('Unknown method')

    return result.tolist()