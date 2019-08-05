import math
import time

import numpy as np

w = np.array((
    [0, 3, 8, np.inf, -4],
    [np.inf, 0, np.inf, 1, 7],
    [np.inf, 4, 0, np.inf, np.inf],
    [2, np.inf, -5, 0, np.inf],
    [np.inf, np.inf, np.inf, 6, 0],
))

c = w
for k in range(5):
    for i in range(5):
        for j in range(5):
            c[i][j] = min(c[i][k] + c[k][j], c[i][j])
print(c)
