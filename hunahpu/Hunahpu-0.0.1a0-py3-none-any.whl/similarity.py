from nltk import ngrams
from unidecode import unidecode


def jc_similarity(title1, title2, n=3, boolean=False, threshold=0.8):
    '''
    Computes titles similarity according to section 2.6 of
    https://arxiv.org/pdf/1911.02782.pdf

    Parameters
    ----------
    title1 : str
        text to compare
    title2 : str
        second text to compare
    n : int (optional)
        number n in n-gram partition of titles
    boolean : bool
        If you want the output to be a bool
    threshold : float
        Threshold for the boolean outpput

    Returns
    -------
    similarity : float/bool
        Number between 0 and 1. 1 means the titles are the same and 0 means completely different
        Or True if similarity is avobe threshold, false otherwise
    '''
    title1 = unidecode(title1.lower())
    title2 = unidecode(title2.lower())
    n1 = ngrams(title1.split(), n)
    n2 = ngrams(title2.split(), n)
    n1 = set(n1)
    n2 = set(n2)
    J = len(n1.intersection(n2))/len(n1.union(n2))
    C = len(n1.intersection(n2))/min([len(n1), len(n2)])
    S = 2*J*C/(J+C)
    if boolean:
        if S >= threshold:
            return True
        else:
            return False
    else:
        return S
