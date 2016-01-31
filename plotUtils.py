#!/usr/bin/python
# -*-coding:utf-8-*-

import types

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import moviepy.editor as mpy
from moviepy.video.io.bindings import mplfig_to_npimage

from Constants import *
from plotACofRadius import firstPeakAC, firstPeakFFT2
from utils import *
from plotsetting import *

def meanOfList(list):
    return np.mean(list)

def firingRate(list):
    return 1000.0 * np.mean(np.reciprocal(list))
class visualize:
    def __init__(self, input_config):
        self.input_config = input_config
        #0.input_method 1.proc_method 2. ylabel 3.filename_postfix 4 legend(optional)
        self.proc_indicator={
            'NetISI':[self.input_config.inputAverISI,meanOfList,'Average ISI of Network','NetISI'],
            'ISI1':[self.input_config.inputAverISIType1,meanOfList,'Average ISI of different types','NetISIForIAndII','Type I'],
            'ISI2':[self.input_config.inputAverISIType2,meanOfList,'Average ISI of different types','NetISIForIAndII','Type II'],
            'Fre':[self.input_config.inputAverISI,firingRate,'average frequency','FiringRate'],
            'Fre1':[self.input_config.inputAverISIType1,firingRate,'average frequency','FiringRateForIAndII','Type I'],
            'Fre2':[self.input_config.inputAverISIType2,firingRate,'average frequency','FiringRateForIAndII','Type II'],
            'CV':[self.input_config.inputCV,meanOfList,'average CV of Network','NetCV'],
            'CV1':[self.input_config.inputCVType1,meanOfList,'average CV','NetCVForIAndII','Type I'],
            'CV2':[self.input_config.inputCVType2,meanOfList,'average CV','NetCVForIAndII','Type II'],
            'PhaseOrder':[self.input_config.inputPhaseAmplitude,meanOfList,'synchronization index','PhaseOrder'],
            'AutoCorrSNR':[self.input_config.inputAverAutoCorrList,firstPeakAC,'$\mathrm{SNR}_\mathrm{cc}$','AutoCorrSNR'],
            'SSFSNR':[self.input_config.inputAverSSFList,firstPeakFFT2,'$\mathrm{SNR}_\mathrm{cp}$','SSFSNR']
        }

    def set_input_config(self, input_config):
        self.input_config = input_config

    def _getFileConfFunc(self, key):
        func_name = FUNC_SET_PREFIX + key
        func = getattr(self.input_config.file_configure, func_name)
        return func

    def testPlot(self):
        plt.plot([1, 2, 3])
        plt.title("TITLE")
        plt.xlabel("XLABEL")
        plt.ylabel("YLABEL")
        plt.savefig('/Users/yes/saved_pic')

    # animation
    def contourGif(self):
        duration = 6
        size = len(time_array)
        fig = plt.figure()

        # DRAW A FIGURE WITH MATPLOTLIB
        def make_frame(t):
            plt.clf()

            im = plt.contourf(data[int(t * size / duration)])
            plt.clim(-60, 40)
            plt.colorbar()

            def setvisible(self, vis):
                for c in self.collections: c.set_visible(vis)

            im.set_visible = types.MethodType(setvisible, im)
            im.axes = plt.gca()

            plt.title(self.input_config.plot_title,fontsize=15)
            return mplfig_to_npimage(fig)

        data = []
        for time in time_array:
            d = self.input_config.inputSpiralWave(time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation = mpy.VideoClip(make_frame, duration=duration)
        # plt.title(self.plot_title)
        checkDirExists(self.input_config)
        animation.write_gif(os.path.join(self.input_config.visual_direct, u'%s.gif' % self.input_config.spec), fps=20)
        del animation
        del data[:]
        plt.close()

    def contourGifOfSeed(self,seed):
        duration = 6
        size = len(time_array)
        fig = plt.figure()

        # DRAW A FIGURE WITH MATPLOTLIB
        def make_frame(t):
            plt.clf()

            im = plt.contourf(data[int(t * size / duration)])
            plt.clim(-60, 40)
            plt.colorbar()

            def setvisible(self, vis):
                for c in self.collections: c.set_visible(vis)

            im.set_visible = types.MethodType(setvisible, im)
            im.axes = plt.gca()

            plt.title(self.input_config.plot_title)
            return mplfig_to_npimage(fig)

        data = []
        for time in time_array:
            d = self.input_config.inputSpiralWaveOfSeed(seed,time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation = mpy.VideoClip(make_frame, duration=duration)
        # plt.title(self.plot_title)
        checkDirExists(self.input_config)
        animation.write_gif(os.path.join(self.input_config.visual_direct, u'%s_Seed=%d.gif' % (self.input_config.spec,seed)), fps=20)
        del animation
        del data[:]
        plt.close()
    def plotSpiralWave(self,time,title):
        mpl.rcParams.update(paramsForSpatialPattern)
        data = self.input_config.inputSpiralWave(time)
        plt.clf()
        plt.contourf(data)
        plt.xlabel('Network Column Index')
        plt.ylabel('Network Row Index')
        plt.xticks([0,32,64,96,127])
        plt.yticks([0,32,64,96,127])
        ax = plt.gcf().gca()
        a=ax.get_xticks().tolist()
        a[0]='1'
        a[4]='128'
        ax.set_xticklabels(a)
        ax.set_yticklabels(a)
        plt.title(self.input_config.plot_title)
        plt.clim(-60, 40)
        cbar = plt.colorbar()
        plt.title(title,y=1.02)
        plt.subplots_adjust(left = 0.15,bottom = 0.15,right = 0.9,top = 0.9)

        checkDirExists(self.input_config)
        plt.savefig(os.path.join(self.input_config.visual_direct, u'%s_t=%.5f_SpatialPattern.png' \
                                 % (self.input_config.spec, time)))
        del data
        del cbar
    def plotSpiralWaves(self, listoftime=time_array):
        filter_array = listoftime[-25:]  # filter(lambda x:int(x)>4500,time_array)
        plt.clf()
        for t in filter_array:
            data = self.input_config.inputSpiralWave(t)
            plt.clf()
            plt.contourf(data)
            plt.xlabel('Network Column Index')
            plt.ylabel('Network Row Index')
            plt.title(self.input_config.plot_title)
            plt.clim(-60, 40)
            cbar = plt.colorbar()
            # plt.show()
            checkDirExists(self.input_config)
            plt.savefig(os.path.join(self.input_config.visual_direct, u'%s_t=%.5f_SpatialPattern.png' \
                                     % (self.input_config.spec, t)))
            del data
            del cbar
        # plt.close()

    def plotTimeSeries(self):
        data = self.input_config.inputTimeSeries()
        #        print data
        column = np.size(data[0, :])
        fig = plt.figure()
        plt.clf()
        plt.subplot(211)
        plt.plot(data[20000:, 0], data[20000:, 1])
        plt.title(self.input_config.plot_title)
        plt.ylabel(u'type I voltage(mV)')
        plt.subplot(212)
        plt.plot(data[20000:, 0], data[20000:, column / 2 + 1])
        plt.ylabel(u'type II voltage(mV)')
        plt.xlabel(u'time(ms)')
        #        plt.title(self.plot_title)
        checkDirExists(self.input_config)
        plt.savefig(os.path.join(self.input_config.visual_direct, u'%s_TimeSeries.tiff' % self.input_config.spec),
                    format='png')
        plt.close()

    def plotAverSSF(self):
        # todo
        mpl.rcParams.update(paramsForSurface)

        fig = plt.figure()
        ax = Axes3D(fig)
        X = range(1,65)
        Y = range(1,65)
        X, Y = np.meshgrid(X, Y)
        # R = np.sqrt(X**2 + Y**2)
        data = self.input_config.inputAverSSF()

        ax.plot_surface(X, Y, data, rstride=1, cstride=1, cmap='Blues_r')
        ax.set_title('(a)')
        ax.set_xlabel(r'$k_x$')
        ax.set_ylabel(r'$k_y$')
        # ax.set_xticklabels()
        # ax.zaxis.set_scale('log')
        zticks = ax.get_zticklabels()
        # ax.set_zticks(np.log10(zticks))
        ax.set_zticklabels(zticks)
        ax.set_zscale('log')
        ax.set_xlim([1,64])
        ax.set_ylim([1,64])
        plt.show()
        checkDirExists(self.input_config)
        # plt.savefig(os.path.join(self.input_config.visual_direct, u'%s_AverSSF.tiff' % self.input_config.spec))


    def plotAverAutoCorr(self):
        # todo
        data = self.input_config.inputAverAutoCorr()

    def plotAverSSFList(self,title_str=""):
        mpl.rcParams.update(paramsForList)
        data = self.input_config.inputAverSSFList()
        fig = plt.figure()
        plt.clf()
        plt.plot(data[:,0],data[:,1])
        plt.xlabel('$r$')
        plt.ylabel('$cp$')
        plt.yscale('log')
        checkDirExists(self.input_config)
        plt.title(title_str,y = 1.02)
        plt.subplots_adjust(left = 0.15,bottom = 0.15,right = 0.9,top = 0.9)
        ytickss = plt.yticks()[0]
        if ytickss[-1] == ytickss[::2][-1]:
            plt.yticks(ytickss[::2])
        elif ytickss[-1] == ytickss[::3][-1]:
            plt.yticks(ytickss[::3])
        elif ytickss[-1] == ytickss[::5][-1]:
            plt.yticks(ytickss[::5])
        plt.savefig(os.path.join(self.input_config.visual_direct, '%s_AverSSFList.tiff' % self.input_config.spec),dpi=50)
        plt.close()

    def plotAverAutoCorrList(self,title_str=''):
        mpl.rcParams.update(paramsForList)
        data = self.input_config.inputAverAutoCorrList()
        fig = plt.figure()
        plt.clf()
        plt.plot(data)
        plt.xlabel('$r$')
        plt.ylabel('$cc$')
        checkDirExists(self.input_config)
        plt.title(title_str,y = 1.02)
        plt.subplots_adjust(left = 0.15,bottom = 0.14,right = 0.9,top = 0.9)
        plt.yticks([-0.2,0.4,1])
        plt.savefig(os.path.join(self.input_config.visual_direct, '%s_AverAutoCorrList.tiff' % self.input_config.spec),dpi=50)
        plt.close()

    def plotSquareForLowISI(self):
        data = self.input_config.inputAverISI()
        sorted_index = sorted(range(len(data)), key=lambda k: data[k])
        num_of_lowest = 30
        dim = int(np.sqrt(len(data)) + 0.5)
        fig = plt.figure()
        plt.clf()
        for index in range(num_of_lowest):
            plt.scatter(sorted_index[index] % dim, sorted_index[index] / dim, s=1)
        plt.text(20,-15,'HighISI=%.5f_LowISI=%.5f'%(np.max(data),np.min(data)),color='r')

        plt.xlim([-1, dim])
        plt.ylim([-1, dim])
        plt.title(self.input_config.plot_title)
        checkDirExists(self.input_config)
        plt.savefig(os.path.join(self.input_config.visual_direct, '%s_LowISILocation.png' % self.input_config.spec),
                    format='png')
        plt.close()

    ###The composite operation
    def plotIndicator(self, key1,value1, title="",key2=None,value2=None,*indicators):
        mpl.rcParams.update(paramsForIndicator)

        fig = plt.figure()
        plt.clf()
        func1 = self._getFileConfFunc(key1)

        plot_line_index = 0

        Out=[]


        if not key2==None:
            if not len(indicators) == 1:
                raise ValueError('If exists key2, indicators should not have two or more elements')
            func2 = self._getFileConfFunc(key2)
            for val2 in value2:
                func2(val2)
                quant = []
                if key2 == 'p_inh' and key1 == 'p_ml1':
                    value1 = conf[val2]
                for val1 in value1:
                     func1(val1)
                     data = self.proc_indicator[indicators[0]][0]()
                     computeddata = data
                     if indicators[0] == 'SSFSNR':
                         computeddata = data[:,1]
                     indic = self.proc_indicator[indicators[0]][1](computeddata)
                     quant.append(indic)
                     Out.append([val1,indic])

                #todo legend
                print quant

                plt.plot(value1,quant,plotCharacter[plot_line_index])
                plot_line_index+=1

            labels = []
            for val2 in value2:
                    labels.append(keyToLegend[key2][0] + r'$\mathrm{%s}$'%str(val2) + keyToLegend[key2][1])
            plt.legend(loc='best',labels =labels)

        else:
            if key1 == 'inh':
                value1=conf[self.input_config.file_configure.p_inh]
            for indicator in indicators:
                quant = []
                for val1 in value1:
                    func1(val1)
                    data = self.proc_indicator[indicator][0]()
                    indic = self.proc_indicator[indicator][1](data)
                    quant.append(indic)
                    Out.append([val1,indic])
                #todo legend
                plt.plot(value1, quant,plotCharacter[plot_line_index])
                plot_line_index+=1
            if len(indicators) > 1:
                labels = []
                for indicator in indicators:
                    labels.append(self.proc_indicator[indicator][4])
                plt.legend(loc='best',labels =labels)

        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        #todo title and legend
        plt.title(title,y = 1.02)
        plt.subplots_adjust(left = 0.15,bottom = 0.14,right = 0.9,top = 0.9)
        plt.xlabel(makeXLabel(key1))
        plt.ylabel(self.proc_indicator[indicators[0]][2])

        if indicators[0]=='AutoCorrSNR':
            ylim_min = plt.ylim()[0]
            ylim_max = plt.ylim()[1]

            ylim_max_new = ylim_max + 0.5*(ylim_max-ylim_min)
            plt.ylim([ylim_min,ylim_max_new])
        #sparse yticks
        max_yticks = 5
        yloc = plt.MaxNLocator(max_yticks)
        plt.gca().yaxis.set_major_locator(yloc)
        if not key2 == None:
            midname = composeFileName(self.input_config,key1,key2)
        else:
            midname = composeFileName(self.input_config,key1)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_%s.png' % (midname,\
                                                            self.proc_indicator[indicators[0]][3])))
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_%s.dat' % (midname,\
                                                            self.proc_indicator[indicators[0]][3])),dataOut)
        plt.close()


    def plotFiringRate(self, key, value, xlabel=""):
        fig = plt.figure()
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputAverISI()
            quant.append(1000.0 * np.mean(np.reciprocal(data)))
        plt.plot(value, quant)
        #        plt.title('(a)')
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'Population Firing Rate(Hz)')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_FiringRate' % midname))
        plt.close()
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_FiringRate.dat' % midname),
                   data)

    def plotFiringRateForIandII(self, key, value, xlabel=""):
        fig = plt.figure()
        plt.clf()
        func = self._getFileConfFunc(key)
        quant1 = []
        quant2 = []
        for i, val in enumerate(value):
            func(val)
            data1 = self.input_config.inputAverISIType1()
            data2 = self.input_config.inputAverISIType2()
            quant1.append(1000.0 * np.mean(np.reciprocal(data1)))
            quant2.append(1000.0 * np.mean(np.reciprocal(data2)))
        plt.plot(value, quant1)
        plt.plot(value, quant2)
        #        plt.title('(a)')
        # todo legend
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'Population Firing Rate(Hz)')
        midname = composeFileName(key, self.input_config)
        plt.savefig(
                os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_FiringRateForIandII' % midname))
        plt.close()
        data = listTupleToArray(value, quant1, quant2)
        np.savetxt(
                os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_FiringRateForIandII.dat' % midname),
                data)

    def plotNetISI(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputAverISI()
            quant.append(np.mean(data))
        plt.plot(value, quant)
        #        plt.title('(a)')
        plt.legend(loc='best')
        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'Population average isi')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_NetISI.tiff' % midname))
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_PhaseOrder.dat') % midname,
                   data)

    def plotNetISIForIandII(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant1 = []
        quant2 = []
        for i, val in enumerate(value):
            func(val)
            data1 = self.input_config.inputAverISIType1()
            data2 = self.input_config.inputAverISIType2()
            quant1.append(np.mean(data1))
            quant2.append(np.mean(data2))
        plt.plot(value, quant1)
        plt.plot(value, quant2)
        #        plt.title('(a)')
        # todo legend
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'Population average isi')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_NetISIForIandII' % midname))

        data = listTupleToArray(value, quant1, quant2)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_NetISIForIandII.dat' % midname),
                   data)

    def plotCV(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputCV()
            quant.append(np.mean(data))
        plt.plot(value, quant)
        #        plt.title('(a)')
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'Coherence variance(Hz)')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_CV' % midname))

        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_CV.dat' % midname), data)

    def plotCVForIandII(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant1 = []
        quant2 = []
        for i, val in enumerate(value):
            func(val)
            data1 = self.input_config.inputCVType1()
            data2 = self.input_config.inputCVType2()
            quant1.append(np.mean(data1))
            quant2.append(np.mean(data2))
        plt.plot(value, quant1)
        plt.plot(value, quant2)
        #        plt.title('(a)')
        # todo legend
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'coherence variance')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_CVForIandII.tiff' % midname))

        data = listTupleToArray(value, quant1, quant2)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_CVForIandII.dat' % midname), data)

    def plotPhaseOrder(self, key, value):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputPhaseAmplitude()
            quant.append(np.mean(data))
        plt.plot(value, quant)
        #        plt.title('(a)')
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key))
        plt.ylabel(u'sychronization index')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_PhaseOrder.tiff' % midname))
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_PhaseOrder.dat' % midname), data)

    def plotAutoCorrSNR(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputAverAutoCorrList()
            res = firstPeakAC(data)
            if type(res) == tuple:
                quant.append(res[0])
            else:
                quant.append(res)
        plt.plot(value, quant)
        #        plt.title('(a)')
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'AutoCorrelation function SNR')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_AutoCorrSNR.tiff' % midname))
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_AutoCorrSNR.dat' % midname),
                   data)

    def plotSSFSNR(self, key, value, xlabel=""):
        plt.clf()
        func = self._getFileConfFunc(key)
        quant = []
        for i, val in enumerate(value):
            func(val)
            data = self.input_config.inputAverSSFList()
            res = firstPeakFFT2(data)
            if type(res) == tuple:
                quant.append(res[0])
            else:
                quant.append(res)
        plt.plot(value, quant)
        #        plt.title('(a)')
        plt.legend(loc='best')

        plt.xlabel(makeXLabel(key, xlabel))
        plt.ylabel(u'Spatial structural  function SNR')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_SSFSNR.tiff' % midname))
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_SSFSNR.dat' % midname), data)
