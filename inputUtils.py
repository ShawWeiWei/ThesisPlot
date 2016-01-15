from Constants import *
import os
import numpy as np


class input:
    def __init__(self, file_configure):
        self.file_configure = file_configure
        self.raw_direct = ""
        self.pp_direct = ""
        self.visual_direct = ""
        self.spec = ""


    def updateConfig(self, file_configure):
        self.file_configure = file_configure

    def updateDirect(self):
        self.file_configure.update()
        mid = os.path.join(self.file_configure.coupleType, self.file_configure.conn, self.file_configure.compos)
        self.raw_direct = os.path.join(Raw, mid)
        self.pp_direct = os.path.join(PP, mid)
        self.visual_direct = os.path.join(Visual, mid)
        self.spec = self.file_configure.spec
        # self.plot_title = self.parameter.plot_title

        # input raw data

    def inputTimeSeries(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_TimeSeries.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputCoupleSeries(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_CoupleSeries.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputSpiralWave(self, time):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_t=%.5f.dat' % (self.spec, time))
        data = np.loadtxt(filename)
        return data

    # input processed data
    def inputAutoCorrelation(self, time):
        self.updateDirect()
        #TODO
        filename = os.path.join(self.pp_direct, u'%s_AC.dat' % (self.spec, time))
        data = np.loadtxt(filename)
        return data

    def inputAutoCorrelationAverage(self):
        self.updateDirect()
        filename = os.path.join(self.pp_direct, u'%s_AC_Average.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputFFT(self, time):
        self.updateDirect()
        filename = os.path.join(self.pp_direct, u'%s_FFT.dat' % (self.spec, time))
        data = np.loadtxt(filename)
        return data

    # def inputSpikingIndex(self):
    #     self.updateDirect()
    #     filename = u'%s\\%s_SpikingIndex.dat' % (self.raw_direct, self.spec)
    #     data = open(filename, 'r')
    #     return data

    def inputPhaseAmplitude(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_PhaseAmplitude.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputAverISIType1(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_AverISIType1.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputAverISIType2(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_AverISIType2.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputAverISI(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_AverISI.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputCVType1(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_CVType1.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputCVType2(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_CVType2.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputCV(self):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_CV.dat' % self.spec)
        data = np.loadtxt(filename)
        return data
