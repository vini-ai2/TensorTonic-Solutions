import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    s = np.asarray(x, dtype=float) 
    
    return 1/(1+np.exp(-s))

