import os

import numpy as np

from Constants import *


class input:
    def __init__(self, file_configure):
        self.file_configure = file_configure
        self.raw_direct = ""
        self.pp_direct = ""
        self.visual_direct = ""
        self.spec = ""
        self.plot_title = ""

    def set_file_configure(self, file_configure):
        self.file_configure = file_configure

    def updateDirect(self):
        self.file_configure.update()
        mid = os.path.join(self.file_configure.coupleType, self.file_configure.conn, self.file_configure.compos)
        self.raw_direct = os.path.join(Raw, mid)
        self.pp_direct = os.path.join(PP, mid)
        self.visual_direct = os.path.join(Visual, mid)
        self.spec = self.file_configure.spec
        self.plot_title = self.file_configure.plot_title

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

    def inputSpiralWaveOfSeed(self, seed, time):
        self.updateDirect()
        filename = os.path.join(self.raw_direct, u'%s_Seed=%d_t=%.5f.dat' % (self.spec, seed, time))
        data = np.loadtxt(filename)
        return data

    # input processed data
    def inputAverAutoCorr(self):
        self.updateDirect()
        filename = os.path.join(self.pp_direct, u'%s_AverAutoCorr.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputAverAutoCorrList(self):
        self.updateDirect()
        filename = os.path.join(self.pp_direct, u'%s_AverAutoCorrList.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputAverSSF(self):
        self.updateDirect()
        filename = os.path.join(self.pp_direct, u'%s_AverSSF.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

    def inputAverSSFList(self):
        self.updateDirect()
        filename = os.path.join(self.pp_direct, u'%s_AverSSFList.dat' % self.spec)
        data = np.loadtxt(filename)
        return data

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
