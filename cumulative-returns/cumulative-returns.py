def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    r_cum = [returns[0]]
    for i, value in enumerate(returns[1:]):
        r_cum.append((r_cum[i] + 1) * (value + 1) - 1)
    return r_cum