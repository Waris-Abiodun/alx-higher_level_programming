def multiple_returns(sentence):
    """
    a function that return lenth of a sentence and its first character
    Args:
        sentence - the sentence to read
    Return:
        (lenght, first_char)
    """
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]
