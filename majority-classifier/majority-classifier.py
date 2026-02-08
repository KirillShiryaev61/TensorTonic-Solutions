import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    train = np.asarray(y_train)
    test = np.asarray(X_test)
    
    unique, counts = np.unique(train, return_counts=True)
    major_class = train[np.argmax(counts)]

    return np.full((test.shape[0],), major_class)