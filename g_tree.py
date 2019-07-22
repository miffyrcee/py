class g_node():
    def __init__(self, key, rank=0, p=None):
        self.key = key
        self.p = p
        if p is not None:
            self.rank = self.p.rank + 1
        else:
            self.rank = rank


root = g_node(1)
t = g_node(12, p=root)
print(t.rank)
