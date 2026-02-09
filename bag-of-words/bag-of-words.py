import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    vocab_dct = {word: idx for idx, word in enumerate(vocab)}
    vector = np.zeros(len(vocab), dtype=int)

    for word in tokens:
        idx = vocab_dct.get(word)
        if idx is not None:
            vector[idx] += 1
    
    return vector