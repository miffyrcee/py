import math
import time

import numpy as np

MAXLENGTH = 1000
w = np.array((
    [0, 3, 8, np.inf, -4],
    [np.inf, 0, np.inf, 1, 7],
    [np.inf, 4, 0, np.inf, np.inf],
    [2, np.inf, -5, 0, np.inf],
    [np.inf, np.inf, np.inf, 6, 0],
))

stack = [0] * 5


def exist_p(u, v, curl):
    if w[u][v] and w[u][v] < MAXLENGTH:
        return stack
    else:
        for i in range(5):
            if w[u][i] and w[u][i] < MAXLENGTH:
                stack[curl] = i
                exist_p(i, v, curl + 1)
        return False


for i in range(5):
    for j in range(5):
        print(exist_p(i, j, 1))
