import pandas as pd

word_list = pd.read_table('~/Downloads/cc.scel', header=None, usecols=[0x83])

print(word_list)
