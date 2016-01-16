import os

import numpy as np

from scipy.signal import correlate2d
#-*-coding:utf-8-*-


def _checkDirExists(dir):
    if os.path.exists(dir):
        pass
    else:
        os.makedirs(dir)


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


def procSSF(averSSF):
    averSSF = np.fft.fftshift(averSSF)
    # add a line and row in the middle
    s = averSSF.shape
    n = s[0]
    # SS = [S(1:n / 2, 1:n);zeros(1, n);S(n / 2 + 1:n, 1:n)]
    # SSS = [SS(1:n + 1, 1:n / 2), zeros(n + 1, 1), SS(1:n + 1, n / 2 + 1:n)];
    SS = np.concatenate((averSSF[:n/2,:], np.zeros([1,n]), averSSF[n/2:,:]), axis=0)
    SSS = np.concatenate((SS[:,:n/2], np.zeros([n+1,1]), SS[:,(n/2):]), axis=1)
    return SSS


def _makeXLabel(key):
    if key == "gc_exc":
        return "excitatory coupling intensity"
    elif key == "gc_inh":
        return "inhibitory coupling intensity"
    elif key == "v_exc":
        return "excitory voltage"
    elif key == "v_inh":
        return "inhibitory voltage"
    elif key == "threshold":
        return "threshold"
    elif key == "p":
        return "rewiring probability"
    elif key == "p_ml1":
        return "the percentage of ml1"
    elif key == "p_ml2":
        return "the percentage of ml2"
    else:
        raise ValueError

def makeXLabel(key, xlabel):
    if xlabel == "":
        return _makeXLabel(key)
    else:
        return xlabel
