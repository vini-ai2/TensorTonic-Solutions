import math
import numpy as np
def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    L = math.sqrt(6/fan_in)
    Wa = np.asarray(W)
    WT = Wa*(2*L)-L
    return WT