import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_predi = np.array(y_pred)
    y_truei = np.array(y_true)
    n =len(y_predi)
    
    mse = (np.mean((y_predi - y_truei)**2))
    return mse    
    pass
