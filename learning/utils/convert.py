import numpy as np


def vectorize_string(s):
    unique=(set(s))
    char2num={u:i for i, u in enumerate(unique)}
    new=[]
    for char in range(len(s)):
        new.append(char2num[s[char]])
    new=np.array(new)
    return new
