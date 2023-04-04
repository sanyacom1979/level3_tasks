import numpy as np


def read_matrix() -> list:
    return np.load(open("matrix_distance", "rb"))
