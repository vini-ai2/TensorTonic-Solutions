import numpy as np

def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    X_1 = np.asarray(X)
    W_1 = np.asarray(W)
    b_1 = np.asarray(b)

    

    return (X_1 @ W_1 + b_1).tolist()