#!/usr/bin/python
# -*-coding:utf-8-*-

from fileconf import *
from inputUtils import *
from plotUtils import *
from procUtils import process

def TestExcitatorySquare():
    file_conf = ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.27]#[0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    aSeed = [2,4,3,6]
    for ml1 in aML1:
        file_conf.set_p_ml1(ml1)
        for seed in aSeed:
             plot_util.contourGifOfSeed(seed)
            # plot_util.plotSpiralWaves()
            # proc_util.averSSF()
            # proc_util.averSSFList()
            # proc_util.averAutoCorr()
            # proc_util.averAutoCorrList()
            # plot_util.plotAverAutoCorrList()
            # plot_util.plotAverSSFList()
            # plot_util.plotSquareForLowISI()

def ExcitatorySquare():
    file_conf = ExcitoryCouple(50, 0.22, 36, -25, "Square")
    aGc = [0.32]#0.22,0.27,0.32]#[0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    # plot_util.plotIndicator('p_ml1',aML1,"(a)",'gc_exc',[0.22,0.27,0.32],'AutoCorrSNR')
    # plot_util.plotIndicator('p_ml1',aML1,"(b)",'gc_exc',[0.22,0.27,0.32],'SSFSNR')
    # file_conf.set_gc_exc(0.22)
    # plot_util.plotIndicator('p_ml1',aML1,"(a)",None,None,'Fre1','Fre2')
    # plot_util.plotIndicator('p_ml1',aML1,"(b)",None,None,'CV1','CV2')
    #
    # file_conf.set_gc_exc(0.27)
    # plot_util.plotIndicator('p_ml1',aML1,"(c)",None,None,'Fre1','Fre2')
    # plot_util.plotIndicator('p_ml1',aML1,"(d)",None,None,'CV1','CV2')
    #
    # file_conf.set_gc_exc(0.32)
    # plot_util.plotIndicator('p_ml1',aML1,"(e)",None,None,'Fre1','Fre2')
    # plot_util.plotIndicator('p_ml1',aML1,"(f)",None,None,'CV1','CV2')

    proc_util = process(input_util)
    aML1=[1]#,20,25,35,40,45,50,60,99]
    # title_list=['(a)','(d)','(g)','(j)','(m)']
    for i,ml1 in enumerate(aML1):
        file_conf.set_p_ml1(ml1)
        for gc_exc in aGc:
            file_conf.set_gc_exc(gc_exc)
            # plot_util.plotSpiralWave(dictExcitatorySquare_0_32[ml1],title_list[i])
            plot_util.contourGif()
            # plot_util.plotSpiralWaves()
            # proc_util.averSSF()
            # plot_util.plotAverSSF()
            # proc_util.averSSFList()
            # proc_util.averAutoCorr()
            # proc_util.averAutoCorrList()
            # plot_util.plotAverAutoCorrList(title_list[2*i])
            # plot_util.plotAverSSFList(title_list[2*i+1])
            # plot_util.plotSquareForLowISI()

def ExcitatorySparser():
    file_conf = ExcitoryCouple(45, 0.27, 36, -25,
                               "Sparser")  # ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.27]  # [0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    #global aML1
    # aP = [0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05,
    # 0.055, 0.06, 0.065, 0.07, 0.075, 0.08,0.085, 0.09,0.095,0.1]
    # aML1=[1,20,35,45,70]
    aP = [0,0.5,0.6]#[0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    # plot_util.plotIndicator('p_ml1',aML1,"(b)",'p',[0.15,0.3],'PhaseOrder')

    # file_conf.set_p(0.15)
    # plot_util.plotIndicator('p_ml1',aML1,"(a)",None,None,'Fre1','Fre2')
    # file_conf.set_p(0.3)
    # plot_util.plotIndicator('p_ml1',aML1,"(b)",None,None,'CV1','CV2')
    i=0
    title_list=['(b)','(c)','(e)','(f)','(h)','(i)','(k)','(l)','(n)','(o)']
    title_time=[7540,7820,7660,7760,7840,7940,7980,7980,7980,7980]
    aML1=[95]
    for ml1 in aML1:
        file_conf.set_p_ml1(ml1)
        for p in aP:
            file_conf.set_p(p)
            # plot_util.plotSpiralWave(title_time[i],title_list[i])
            # i+=1
            plot_util.contourGif()
            plot_util.plotSpiralWaves()
            proc_util.averSSF()
            proc_util.averSSFList()
            proc_util.averAutoCorr()
            proc_util.averAutoCorrList()
            plot_util.plotAverAutoCorrList()
            plot_util.plotAverSSFList()

def InhibitorySquare():
    file_conf = InhibitoryCouple(45, 54, 0.27, 0.27, 36, -45, -25,
                                 "Square")  # ExcitoryCouple(50, 0.27, 36, -25, "Square")
    aGc = [0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31,
           0.32]  # [0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    proc_util = process(input_util)
    # plot_util.plotIndicator('p_ml1',aML1,"(a)",'p_inh',[2,4,6],'PhaseOrder')
    #
    # file_conf.set_gc_exc(0.27)
    # plot_util.plotIndicator('p_ml1',aML1,"(c)",None,None,'Fre1','Fre2')
    # plot_util.plotIndicator('p_ml1',aML1,"(d)",None,None,'CV1','CV2')

    # aML1 = [1,20,35,45,70]
    aInh = [0,10]
    i=0
    # title_list=['(b)','(e)','(h)','(k)','(n)','(c)','(f)','(i)','(l)','(o)']
    title_time=[7780,7840,7980,7880,7980,7960,7840,7980,7860,7980]
    for inh in aInh:
        file_conf.set_p_inh(inh)
        for ml1 in conf[inh]:
            file_conf.set_p_ml1(ml1)

            # plot_util.contourGif()
            plot_util.plotSpiralWave(title_time[i],title_list[i])
            i+=1
            # plot_util.plotSpiralWaves()
            # proc_util.averSSF()
            # proc_util.averSSFList()
            # proc_util.averAutoCorr()
            # proc_util.averAutoCorrList()
            # plot_util.plotAverAutoCorrList()
            # plot_util.plotAverSSFList()

def InhibitorySparser():
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
        for ml1 in conf[inh]:
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
    # file_conf = ExcitoryCouple(50, 0.27, 36, -25, "Square")
    # aGc = [0.27]#[0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32]
    # input_util = input(file_conf)
    # plot_util = visualize(input_util)
    # proc_util = process(input_util)
    # plot_util.plotIndicator('p_ml1',aML1,"",'gc_exc',[0.23,0.24,0.25],'CV')
    ExcitatorySquare()
    # InhibitorySquare()
    # ExcitatorySparser()
    # InhibitorySquare()