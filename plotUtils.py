#!/usr/bin/python
# -*-coding:utf-8-*-
from inputUtils import input
from Constants import *
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import matplotlib.pyplot as plt
from utils import *
import types
import os
import plotsetting


class visualize:
    def __init__(self, input_config):
        self.input_config = input_config

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

            # plt.title(self.plot_title)
            return mplfig_to_npimage(fig)

        data = []
        for time in time_array:
            d = self.input_config.inputSpiralWave(time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation = mpy.VideoClip(make_frame, duration=duration)
        # plt.title(self.plot_title)
        self._checkDirExists()
        animation.write_gif(os.path.join(self.input_config.visual_direct, u'%s.gif' % self.input_config.spec), fps=20)

    def plotSpiralWaves(self, listoftime=time_array):
        filter_array = listoftime[-25:]  # filter(lambda x:int(x)>4500,time_array)    
        for t in filter_array:
            data = self.input_config.inputSpiralWave(t)
            plt.clf()
            plt.contourf(data)
            plt.xlabel('Network Column Index')
            plt.ylabel('Network Row Index')
            plt.clim(-60, 40)
            cbar = plt.colorbar()
            checkDirExists(self.input_config.visual_direct)
            plt.savefig(os.path.join(self.input_config.visual_direct,
                                     u'%s_t=%.5f_SpatialPattern' % (self.input_config.spec_out, t)))
            del cbar

    def plotTimeSeries(self):
        data = self.input_config.inputTimeSeries()
        #        print data
        column = np.size(data[0, :])
        plt.clf()
        plt.subplot(211)
        plt.plot(data[20000:, 0], data[20000:, 1])
        plt.title(self.plot_title)
        plt.ylabel(u'type I voltage(mV)')
        plt.subplot(212)
        plt.plot(data[20000:, 0], data[20000:, column / 2 + 1])
        plt.ylabel(u'type II voltage(mV)')
        plt.xlabel(u'time(ms)')

        #        plt.title(self.plot_title)
        checkDirExists(self.Visualdirect)
        plt.savefig(os.path.join(self.Visualdirect, u'%s_TimeSeries.png' % (self.coupleAndNoise)))

    def plotFiringRate(self, key, value, xlabel=""):
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

        makeXLabel(key, xlabel)
        plt.ylabel(u'Population Firing Rate(Hz)')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_FiringRate' % midname))

        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_FiringRate.txt' % midname),
                   data)

    def plotFiringRateForIandII(self, key, value, xlabel=""):
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

        makeXLabel(key, xlabel)
        plt.ylabel(u'Population Firing Rate(Hz)')
        midname = composeFileName(key, self.input_config)
        plt.savefig(
            os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_FiringRateForIandII' % midname))

        data = listTupleToArray(value, quant1, quant2)
        np.savetxt(
            os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_FiringRateForIandII.txt' % midname),
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

        makeXLabel(key, xlabel)
        plt.ylabel(u'Coherence variance(Hz)')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_CV' % midname))

        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_CV.txt' % midname),
                   data)

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

        makeXLabel(key, xlabel)
        plt.ylabel(u'coherence variance')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_CVForIandII' % midname))

        data = listTupleToArray(value, quant1, quant2)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_CVForIandII.txt' % midname),
                   data)

    def plotPhaseOrder(self, key, value, xlabel=""):
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

        makeXLabel(key, xlabel)
        plt.ylabel(u'sychronization index')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_PhaseOrder' % midname))
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_PhaseOrder.txt' % midname),
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

        makeXLabel(key, xlabel)
        plt.ylabel(u'Population average isi')
        midname = composeFileName(key, self.input_config)
        plt.savefig(os.path.join(Visual, self.input_config.file_configure.coupleType, u'%s_NetISI' % midname))
        data = listTupleToArray(value, quant)
        np.savetxt(os.path.join(PP, self.input_config.file_configure.coupleType, u'%s_PhaseOrder.txt') % midname,
                   data)
