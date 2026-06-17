import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a1 = np.array(a, float)
    b1 = np.array(b, float)
    anorm = np.sqrt(np.dot(a, a))
    bnorm = np.sqrt(np.dot(b, b))
    if anorm == 0.0 or bnorm == 0.0:
        return 0.0
    sim = np.dot(a, b)/(anorm * bnorm)
    return sim
    pass