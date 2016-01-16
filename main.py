#!/usr/bin/python
#-*-coding:utf-8-*-

from fileconf import *
from inputUtils import *
from plotUtils import *
from utils import *
from procUtils import *
def com(averSSF):
    s = averSSF.shape
    n = s[0]
    # SS = [S(1:n / 2, 1:n);zeros(1, n);S(n / 2 + 1:n, 1:n)]
    # SSS = [SS(1:n + 1, 1:n / 2), zeros(n + 1, 1), SS(1:n + 1, n / 2 + 1:n)];
    SS = np.concatenate((averSSF[:n/2,:], np.zeros([1,n]), averSSF[n/2:,:]), axis=0)
    SSS = np.concatenate((SS[:,:n/2], np.zeros([n+1,1]), SS[:,(n/2):]), axis=1)
    return SSS

if __name__ == "__main__":
    file_conf = ExcitoryCouple(50, 0.25, 36, -25, "Square")
    input_util = input(file_conf)
    proc_util = process(input_util)
   # proc_util.averAutoCorr()
   # proc_util.averAutoCorrList()
    proc_util.averSSF()
    proc_util.averSSFList()

    plot_util = visualize(input_util)
    # plot_util.plotTimeSeries()
   # plot_util.contourGif()
    plot_util.plotAverAutoCorr()
    plot_util.plotAverAutoCorrList()
    plot_util.plotAverSSF()
    plot_util.plotAverSSFList()



    #plot_util.plotSpiralWaves()
    # plot_util.testPlot()
    keyvalue = {"gc_ex":[1,2,3]}








