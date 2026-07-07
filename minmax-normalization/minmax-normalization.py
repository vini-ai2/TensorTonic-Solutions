import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X = np.asarray(X, dtype=float)
    X_min = np.min(X, axis = axis, keepdims=True)
    X_max = np.max(X, axis = axis, keepdims=True)
    X_range = X_max - X_min
    X_range[X_range == 0.0] = eps
    X_scaled = (X - X_min) / X_range
    return X_scaled
    
    pass