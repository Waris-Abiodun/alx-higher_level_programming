def multiple_returns(sentence):
    """
    a function that return lenth of a sentence and its first character
    Args:
        sentence - the sentence to read
    Return:
        len(sentence) - lenght of a sentence
        sentence[0] - the frist letter of the sentence
    """
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]
