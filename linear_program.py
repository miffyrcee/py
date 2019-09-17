import numpy as np

a = np.array((
    [1, -1, -1, -1, -1],
    [0, -2, 8, 0, 10],
    [0, 5, 2, 0, 0],
    [0, 3, -5, 10, 2],
    [0, 1, 1, 1, 1],
))
b = np.array(([1000, 50, 100, 25, 0]))

print(np.linalg.solve(a, b))
