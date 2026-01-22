from collections import Counter

def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    if len(sentences) == 0:
        return {}

    lst = []
    for i in sentences:
        lst.extend(i)
    
    return Counter(lst)
