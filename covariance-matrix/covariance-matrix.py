import numpy as np

def covariance_matrix(X):
    X = np.asarray(X, dtype=float)

    if X.ndim != 2 or X.shape[0] < 2:
        return None

    n = X.shape[0]
    mean = np.mean(X, axis=0, keepdims=True)
    X_centered = X - mean
    cov_matrix = (X_centered.T @ X_centered) / (n - 1)

    return cov_matrix