def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.array(y_true, dtype=np.int64)
    y_pred = np.array(y_pred, dtype=np.int64)

    if y_true.shape[0] != y_pred.shape[0]:
        return None

    labels = np.unique(np.concatenate([y_true, y_pred]))
    tp = fp = fn = 0

    for label in labels:
        tp += np.sum((y_true == label) & (y_pred == label))
        fp += np.sum((y_true != label) & (y_pred == label))
        fn += np.sum((y_true == label) & (y_pred != label))

    if tp + fp + fn == 0:
        return 1.0
    else:
        return 2 * tp / (2 * tp + fp + fn)
