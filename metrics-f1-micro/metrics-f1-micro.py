def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.array(y_true, dtype=np.float64)
    y_pred = np.array(y_pred, dtype=np.float64)

    if y_true.shape[0] != y_pred.shape[0]:
        return None

    tp = sum((y_true == y_pred).astype(int))

    return (2 * tp) / (2 * tp + 2 * (y_true.shape[0] - tp))
