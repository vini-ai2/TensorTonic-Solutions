#import nltk 
#from nltk.tokenize import word_tokenize
#from nltk.corpus import remove_stopwords
def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopwords = set(stopwords)
    filtered_t = []
    for token in tokens:
        if token not in stopwords:
            filtered_t.append(token)

    return filtered_t
    pass