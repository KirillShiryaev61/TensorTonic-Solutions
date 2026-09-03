import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    x = torch.tensor(values, dtype=torch.float32, requires_grad=True)
    y = (x.pow(3) + 2 * x).sum().backward()
    return x.grad.tolist()
