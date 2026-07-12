import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    trace = sum(A[i][i] for i in range(len(A)))
    return trace
    pass
