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
    return str[0:pre + 1] + "(variant)" + str[pre + post:]

def renameSpec(str, key):
    pre = str.index(key) + len(key)
    post = str.split(key)[1].index("_")
    return str[0:pre + 1] + "(variant)" + str[pre + post:]

def renameCompos(str, key):
    if key == "p_ml1":
        compos = renameSpec(str,"pML1")
    elif key == "p_ml2":
        pre = str.index("pML2") + len("pML2")
        compos = str[:pre+1] + "(variant)"
    else:
        raise ValueError
    return compos


def composeFileName(key, input_config):
    filename = input_config.file_configure.conn + '_' + input_config.file_configure.compos + '_' + \
        input_config.file_configure.spec_out
    if key == "gc_exc" or key == "gc_inh" or key == "v_exc" or key == "v_inh" or key == "threshold" or key == 'p':
        return replaceKey(filename,key)
    elif key == "p_ml1":
        return replaceKey(filename, "pML1")
    elif key == "p_ml2":
        return replaceKey(filename, "pML2")
    else:
        raise ValueError