import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x1 = np.array(x, dtype=float)
    y1 = np.array(y, dtype=float)
    d = np.sqrt(np.sum((x1-y1)**2))
    # Write code here
    return d
    pass