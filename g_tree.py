import os

import numpy as np


class dfs_node():
    def __init__(self, d=0, f=0, p=None):
        self.d = d
        self.f = f
