import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.asarray(x, dtype=float)
    res = np.where(x>0, x, alpha*(np.exp(x)-1))
    return res.tolist()
    # if x.any()>0:
    #     return x
    # else:
    #     return alpha*(np.exp(x)-1)