import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x1 = np.array(x, float)
    y1 = np.array(y, float)

    
    mag = np.sum(np.abs(x1- y1))
    return mag
        
    pass