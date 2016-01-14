from Constants import *
import os
import numpy as np

class input:
    def __init__(self, fileconfigure):
        self.fileconfigure = fileconfigure

    def updateConfig(self, config):
        self.parameter = config

    def updateDirect(self):
        self.parameter.update()
        mid = os.path.join(self.parameter.couple, self.parameter.connection, self.parameter.composition)
        self.Rawdirect = os.path.join(Raw, mid)
        self.PPdirect = os.path.join(PP, mid)
        self.Visualdirect = os.path.join(Visual, mid)
        self.coupleAndNoise = self.parameter.coupleAndNoise
        self.plot_title = self.parameter.plot_title

        # input raw data

    def inputTimeSeries(self):
        self.updateDirect()
        filename = u'%s\\%s_TimeSeries.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputCoupleSeries(self):
        self.updateDirect()
        filename = u'%s\\%s_CoupleSeries.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputSpiralWave(self, time):
        self.updateDirect()
        filename = u'%s\\%s_t=%.5f.dat' % (self.Rawdirect, self.coupleAndNoise, time)
        data = np.loadtxt(filename)
        return data

    # input processed data
    def inputAutoCorrelation(self, time):
        self.updateDirect()
        filename = u'%s\\%s_AC.dat' % (self.PPdirect, self.coupleAndNoise, time)
        data = np.loadtxt(filename)
        return data

    def inputAutoCorrelationAverage(self):
        self.updateDirect()
        filename = u'%s\\%s_AC_Average.dat' % (self.PPdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputFFT(self, time):
        self.updateDirect()
        filename = u'%s\\%s_FFT.dat' % (self.PPdirect, self.coupleAndNoise, time)
        data = np.loadtxt(filename)
        return data

    def inputSpikingIndex(self):
        self.updateDirect()
        filename = u'%s\\%s_SpikingIndex.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = open(filename, 'r')
        return data

    def inputPhaseAmplitude(self):
        self.updateDirect()
        filename = u'%s\\%s_PhaseAmplitude.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputAverISIType1(self):
        self.updateDirect()
        filename = u'%s\\%s_AverISIType1.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputAverISIType2(self):
        self.updateDirect()
        filename = u'%s\\%s_AverISIType2.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputAverISI(self):
        self.updateDirect()
        filename = u'%s\\%s_AverISI.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputCVType1(self):
        self.updateDirect()
        filename = u'%s\\%s_CVType1.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputCVType2(self):
        self.updateDirect()
        filename = u'%s\\%s_CVType2.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data

    def inputCV(self):
        self.updateDirect()
        filename = u'%s\\%s_CV.dat' % (self.Rawdirect, self.coupleAndNoise)
        data = np.loadtxt(filename)
        return data
