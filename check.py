import os
import numpy as np


def checkDirExists(dir):
    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir)


def listTupleToArray(*args):
    out = []
    for list in args:
        out.append(list)
    data_out = np.array(out)
    data_out = data_out.transpose()
    return data_out

def replaceKey(str, key):
    pre = str.index(key) + len(key)
    post = str.split(key)[1].index("_")
    print str[0:pre+1] + "(variant)" + str[pre+post:]