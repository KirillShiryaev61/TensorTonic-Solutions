import torch

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """
    pred = torch.tensor(pred, dtype=torch.float32)
    target = torch.tensor(target, dtype=torch.float32)
    delta = torch.tensor(delta, dtype=torch.float32)
    
    if method == 'mse':
        return ((pred - target)**2).mean().item()
    elif method == 'cross_entropy':
        pred = -torch.nn.functional.log_softmax(pred, dim=-1)
        idx = target.unsqueeze(1).int()
        return torch.gather(pred, dim=1, index=idx).mean().item()
    elif method == 'huber':
        error = (target - pred).abs()
        return torch.where(
            error <= delta,
            0.5 * error**2,
            delta * (error - 0.5 * delta)
        ).mean().item()
    else:
        ValueError('Unknown method')
        
