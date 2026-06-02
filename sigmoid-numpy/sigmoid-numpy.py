import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    return 1 / (1 + np.exp(-np.array(x)))
