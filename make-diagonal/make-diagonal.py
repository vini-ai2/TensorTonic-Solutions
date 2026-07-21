import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    #n = np.shape(v) #returns a tuple in the format of (n, )
    n = len(v)
    D = np.zeros((n,n))
    
    
    D = np.diag(v)
    for i in range(n):
        D[i, i] = v[i]
    return D
            
    
    pass
