#!/usr/bin/python
#-*-coding:utf-8-*-

from fileconf import *
from inputUtils import *
from plotUtils import *
from utils import *
from procUtils import process
def com(averSSF):
    s = averSSF.shape
    n = s[0]
    # SS = [S(1:n / 2, 1:n);zeros(1, n);S(n / 2 + 1:n, 1:n)]
    # SSS = [SS(1:n + 1, 1:n / 2), zeros(n + 1, 1), SS(1:n + 1, n / 2 + 1:n)];
    SS = np.concatenate((averSSF[:n/2,:], np.zeros([1,n]), averSSF[n/2:,:]), axis=0)
    SSS = np.concatenate((SS[:,:n/2], np.zeros([n+1,1]), SS[:,(n/2):]), axis=1)
    return SSS

if __name__ == "__main__":
    file_conf = ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    for ml1 in aML1[-12:]:
        file_conf.set_p_ml1(ml1)
        for gc_exc in aGc:
            file_conf.set_gc_exc(gc_exc)
            plot_util.contourGif()
            plot_util.plotSpiralWaves()
            proc_util.averSSF()
            proc_util.averSSFList()
            proc_util.averAutoCorr()
            proc_util.averAutoCorrList()
            plot_util.plotAverAutoCorrList()
            plot_util.plotAverSSFList()








