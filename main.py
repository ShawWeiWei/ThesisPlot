#!/usr/bin/python
#-*-coding:utf-8-*-

from fileconf import *
from inputUtils import *
from plotUtils import *
from utils import *

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
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    #plot_util.plotSpiralWaves()
    # plot_util.testPlot()
    keyvalue = {"gc_ex":[1,2,3]}
    def test(key,value,obj):
        func_name = "set_"+key
        func = getattr(obj,func_name)
        for a in value:
            func(a)

    averSSF = np.array([[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]])

    print com(averSSF)


#    test("gc_ex",[1,2,3],file_conf)
#    listTupleToArray([1,2,3],[2,3,4])


