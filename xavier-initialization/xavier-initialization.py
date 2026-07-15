import math

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    L = math.sqrt(6/(fan_in+fan_out))
    Wa = np.asarray(W)
    WT = Wa*(2*L)-L
    return WT