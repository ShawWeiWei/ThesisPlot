import os

import numpy as np

from scipy.signal import correlate2d

def _checkDirExists(dir):
    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir)


def checkDirExists(input_config):
    _checkDirExists(input_config.visual_direct)
    _checkDirExists(input_config.pp_direct)


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


def composeFileName(key, input_config):
    filename = input_config.file_configure.conn + '_' + input_config.file_configure.compos + '_' + \
               input_config.file_configure.spec_out
    if key == "gc_exc" or key == "gc_inh" or key == "v_exc" or key == "v_inh" or key == "threshold" or key == 'p':
        return replaceKey(filename, key)
    elif key == "p_ml1":
        return replaceKey(filename, "pML1")
    elif key == "p_ml2":
        return replaceKey(filename, "pML2")
    else:
        raise ValueError


def autoCorr(matrix):
    averagePotential = np.mean(matrix)
    matrix = matrix - averagePotential
    matrix = correlate2d(matrix, matrix)
    shape = matrix.shape
    max_ele = matrix[shape[0] / 2, shape[1] / 2]
    return matrix[shape[0] / 2:, shape[1] / 2:] / max_ele
