import numpy as np
import math 

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    e = y_true - y_pred
    err_range = np.abs(e) <= delta
    sq_err = 0.5 * e**2
    lin_loss = delta*(np.abs(e) - 0.5*delta)
    return np.mean(np.where(err_range, sq_err, lin_loss))
    pass