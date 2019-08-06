import math
import string
import time
from random import choice, choices

import numpy as np
from numpy.linalg import *
from numpy.ma import *

n = 5
w = choices(string.digits, k=n * n)
w = np.reshape(w, (n, n)).astype(float)
w = np.where(w == 0, np.inf, w)
for i, j in zip(range(n), range(n)):
    w[i][j] = 0
