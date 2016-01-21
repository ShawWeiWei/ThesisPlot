#!/usr/bin/python
# -*-coding:utf-8-*-

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
    SS = np.concatenate((averSSF[:n / 2, :], np.zeros([1, n]), averSSF[n / 2:, :]), axis=0)
    SSS = np.concatenate((SS[:, :n / 2], np.zeros([n + 1, 1]), SS[:, (n / 2):]), axis=1)
    return SSS


def singlePlotAndProc():
    file_conf = ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    aML1 = [70, 65, 60]
    for ml1 in aML1:
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


conf = [
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 99],
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98],
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 97],
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 96],
    [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
]


def inhibitoryPlotAndProc():
    file_conf = InhibitoryCouple(45, 54, 0.27, 0.27, 36, -45, -25,
                                 "Square")  # ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31,
           0.32]  # [0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    aML1 = [50]
    aInh = [1, 2, 3, 4, 0]
    for inh in aInh:
        for ml1 in conf[inh]:
            file_conf.set_p_ml1(ml1)
            file_conf.set_p_ml2(100 - ml1 - inh)
            plot_util.contourGif()
            plot_util.plotSpiralWaves()
            proc_util.averSSF()
            proc_util.averSSFList()
            proc_util.averAutoCorr()
            proc_util.averAutoCorrList()
            plot_util.plotAverAutoCorrList()
            plot_util.plotAverSSFList()


confSparser = [
    [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99],
    [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 98],
    [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 97],
    [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 96],
    [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
]


def inhibitorySparserPlotAndProc():
    file_conf = InhibitoryCouple(45, 54, 0.27, 0.27, 36, -45, -25,
                                 "Sparser")  # ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31,
           0.32]  # [0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    aP = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    aML1 = [50]
    aInh = [4]
    for inh in aInh:
        for ml1 in confSparser[inh]:
            file_conf.set_p_ml1(ml1)
            file_conf.set_p_ml2(100 - ml1 - inh)
            for p in aP:
                file_conf.set_p(p)
                plot_util.contourGif()
                plot_util.plotSpiralWaves()
                proc_util.averSSF()
                proc_util.averSSFList()
                proc_util.averAutoCorr()
                proc_util.averAutoCorrList()
                plot_util.plotAverAutoCorrList()
                plot_util.plotAverSSFList()


if __name__ == "__main__":
    inhibitorySparserPlotAndProc()
