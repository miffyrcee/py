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


def exist_p(u, v, stack=list()):
    if w[u][v] and w[u][v] < MAXLENGTH:
        print(stack)
        return True
    else:
        for i in range(5):
            if w[u][i] and w[u][i] < MAXLENGTH:
                stack.append(i)
                exist_p(i, v, stack)
        return False


print(exist_p(0, 1))
