# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import types
import os
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from plotACofRadius import *
#import matploblib.mlab as ml
dictLabelOfDifferentProp={15565:'(a)',14746:'(b)',13926:'(c)',13107:'(d)',12288:'(e)',11469:'(f)'\
,10650:'(g)',9830:'(h)',9011:'(i)',8192:'(j)',7373:'(k)',6554:'(l)',5734:'(m)',4915:'(n)',4096:'(o)',3277:'(p)'\
,2458:'(q)',1638:'(r)',819:'(s)'}
listForI=[(1640,'(a)'),(1680,'(b)'),(1700,'(c)'),(1720,'(d)'),(1740,'(e)'),(1760,'(f)')]
dictTimeOfDifferentPropOnlyForThesis={15565:2680,14746:1080,13926:2480,13107:2340,12288:2420,11469:2400,10650:2380,9830:2380\
,9011:2460,8192:2360,7373:2080,6554:2344,5734:2340,4915:2424,4096:2240,3277:2502,2458:2320,1638:2140,819:1780}
listForII=[(2928,'(a)'),(2930,'(a)','(b)'),(2934,'(c)'),(2936,'(d)'),(2956,'b')]
dictHeterSpiralWave_0_22={1:3180,5:3360,10:4880,15:4800,20:4540,25:4640,30:4920,35:4660,40:4760,45:4860,\
50:4980,55:4700,60:4720,65:4660,70:4940,75:4600,80:4680,85:4820,90:4800,95:4760,99:4520}
dictHeterSpiralWave_0_25={1:4680,5:4860,10:4600,15:4960,20:4880,25:4620,30:4800,35:4720,40:4640,45:4920,\
50:4980,55:4660,60:4980,65:4980,70:4980,75:4980,80:4980,85:4980,90:4980,95:4980,99:4980}
BeginForGc={0.22:60,0.23:60,0.24:55,0.25:50,0.26:55,0.27:50,0.28:40,0.29:45,0.3:45,0.31:40,0.33:40}
EndForGc={0.22:70,0.23:70,0.24:65,0.25:65,0.26:60,0.27:60,0.28:55,0.29:60,0.3:55,0.31:55,0.33:50}
anno = {
'text': '$\\sum_{k=0}^{\\infty} \\frac {(-1)^k x^{1+2k}}{(1 + 2k)!}$',
'x': 0.3, 'y': 0.6,'xref': "paper", 'yref': "paper",'showarrow': False,
'font':{'size':24}
}

plotCharacter=['k-','k--','k-.','k:','k*-']
fsize=16
#fig=plt.figure()
time_array=np.linspace(5020,7980,149)
Raw=u'F:\\output'
ExcitatoryCouple=u'ExcitatoryCouple'
CoupleWithInhibition=u'CoupleWithInhibition'
PP=u'F:\\verification\\PP'
Visual=u'F:\\verification\\Visual'
Thesis=u'F:\\Graduation Thesis\\FigureForThesis'
time=np.linspace(2000.1,3000,10000)
def maximumIndex(li):
    maxIndex=0
    maxi=li[0]
    for i,value in enumerate(li):
        if maxi<value:
            maxIndex=i
    return maxIndex
    
def minimumIndex(li):
    minIndex=0
    mini=li[0]
    for i,value in enumerate(li):
        if mini>value:
            miniIndex=i
    return miniIndex
    
#def medianIndex(li):
    
def maximumIndexOfList(li):
    length=len(li)
    if length<3:
        return []
    else:
        retIdx=[]
        for i in range(1,length-1):
            if li[i]>li[i-1] and li[i]>li[i+1] and li[i]>20:
                retIdx.append(i)
        return retIdx
def StringToDoubleArray(String):
    from StringIO import StringIO
    import re
    
    DataArray=np.empty([0])
    doublestring=String.strip()
    if len(doublestring)>0:

        StrIOs=StringIO(doublestring)
        DataArray=np.genfromtxt(StrIOs)
        
    return DataArray
 
  
def genPhase(findex):
    count=len(findex)
    if count<4:
        return 
    else:
        index=[]
        for i in findex:
            index.append(int(i))
        deltat=float(index[count-2]-index[1])/(count-3)
        leftindex=index[0]
        rightindex=index[1] 
        for j in range(leftindex,rightindex):
            yield 2*np.pi*(deltat+j-rightindex)/deltat
 
        
        for m in range(1,count-2):
            leftindex=index[m]
            rightindex=index[m+1]
            dt=float(rightindex-leftindex)
            for j in range(leftindex,rightindex):
                yield 2*np.pi*(j-leftindex)/dt
        
                
        leftindex=index[count-2]
        rightindex=index[count-1]
        for j in range(leftindex,rightindex):
            yield 2*np.pi*(j-leftindex)/deltat
            

class parameterExc:
    def __init__(self,pML1,gc_exc,Vsyn,threshold,con,p=0):
        self.pML1=pML1
        self.gc_exc=gc_exc
        self.Vsyn=Vsyn
        self.threshold=threshold
        self.couple=ExcitatoryCouple
        self.con=con
        self.p=p          
        self.update()
        
    def setGc(self,gc_exc):
        self.gc_exc=gc_exc
        
    def setProp(self,pML1):
        self.pML1=pML1
        
    def setCon(self,con):
        self.con=con
        
    def setP(self,p):
        self.p=p   
                   
    def update(self):
        if self.con=='Square':
            self.connection='Square'
        elif self.con=='SmallWorld':
            self.connection=u'SmallWorld_%.5f'%(self.p)
        elif self.con=='Sparser':
            self.connection=u'Sparser_%.5f'%(self.p)
        else:
            raise ValueError
        self.coupleAndNoise=u'gc=%.5f_Vsyn=%.5f_threshold=%.5f'%(self.gc_exc,self.Vsyn,self.threshold)
        self.composition=u'pML1=%d%%'%(self.pML1)
        self.plot_title=u'pML=%d%%_gc=%.5f'%(self.pML1,self.gc_exc)
      
                    
class parameterInh:
    def __init__(self,pML1,pML2,gc_exc,gc_inh,V_exc,V_inh,threshold,con,p=0):
        self.pML1=pML1
        self.pML2=pML2
        self.gc_exc=gc_exc
        self.gc_inh=gc_inh
        self.V_exc=V_exc
        self.V_inh=V_inh
        self.threshold=threshold
        self.couple=CoupleWithInhibition
        self.con=con
        self.p=p
  
        self.update()

        
    def setGc(self,gc_exc,gc_inh):
        self.gc_exc=gc_exc
        self.gc_inh=gc_inh
        
    def setProp(self,pML1):
        self.pML1=pML1

    def setCon(self,con):
        self.con=con
        
    def setP(self,p):
        self.p=p
                        
    def update(self):
        
        if self.con=='Square':
            self.connection='Square'
        elif self.con=='SmallWorld':
            self.connection=u'SmallWorld_%.5f'%(p)
        elif self.con=='Sparser':
            self.connection=u'Sparser_%.5f'%(p)
        else:
            raise ValueError
        self.coupleAndNoise=u'gc_exc=%.5f_V_exc=%.5f_gc_inh=%.5f_V_inh=%.5f_threshold=%.5f'%\
        (self.gc_exc,self.V_exc,self.gc_inh,self.V_inh,self.threshold)
        self.composition=u'pML1=%d%%_pML2=%d%%'%(self.pML1,self.pML2)
        self.plot_title='pML1=%d%%_pML2=%d%%_gc_exc=%.5f_gc_inh=%.5f'%\
        (self.pML1,self.pML2,self.gc_exc,self.gc_inh)
        
                    
class inputData(object):
    def __init__(self,config):
        self.parameter=config
     
    def updateConfig(self,config):
        self.parameter=config      
    def updateDirect(self):
        self.parameter.update()
        mid=os.path.join(self.parameter.couple,self.parameter.connection,self.parameter.composition)
        self.Rawdirect=os.path.join(Raw,mid)
        self.PPdirect=os.path.join(PP,mid)
        self.Visualdirect=os.path.join(Visual,mid)
        self.coupleAndNoise=self.parameter.coupleAndNoise  
        self.plot_title=self.parameter.plot_title      

    #input raw data
    def inputTimeSeries(self):
        self.updateDirect()
        filename=u'%s\\%s_TimeSeries.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
        
    def inputCoupleSeries(self):
        self.updateDirect()
        filename=u'%s\\%s_CoupleSeries.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
        
    def inputSpiralWave(self,time):
        self.updateDirect()
        filename=u'%s\\%s_t=%.5f.dat'%(self.Rawdirect,self.coupleAndNoise,time)
        data=np.loadtxt(filename)
        return data

    #input processed data
    def inputAutoCorrelation(self,time):
        self.updateDirect()
        filename=u'%s\\%s_AC.dat'%(self.PPdirect,self.coupleAndNoise,time)
        data=np.loadtxt(filename)
        return data
        
    def inputAutoCorrelationAverage(self):
        self.updateDirect()
        filename=u'%s\\%s_AC_Average.dat'%(self.PPdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
        
    def inputFFT(self,time):
        self.updateDirect()
        filename=u'%s\\%s_FFT.dat'%(self.PPdirect,self.coupleAndNoise,time)
        data=np.loadtxt(filename)
        return data
        
    def inputSpikingIndex(self):
        self.updateDirect()
        filename=u'%s\\%s_SpikingIndex.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=open(filename,'r')
        return data
        
    def inputPhaseAmplitude(self):
        self.updateDirect()
        filename=u'%s\\%s_PhaseAmplitude.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
        
    def inputAverISIType1(self):
        self.updateDirect()
        filename=u'%s\\%s_AverISIType1.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
        
    def inputAverISIType2(self):
        self.updateDirect()
        filename=u'%s\\%s_AverISIType2.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
    def inputAverISI(self):
        self.updateDirect()
        filename=u'%s\\%s_AverISI.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data
    def inputCVType1(self):
        self.updateDirect()
        filename=u'%s\\%s_CVType1.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data     
    def inputCVType2(self):
        self.updateDirect()
        filename=u'%s\\%s_CVType2.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data   
    def inputCV(self):
        self.updateDirect()
        filename=u'%s\\%s_CV.dat'%(self.Rawdirect,self.coupleAndNoise)
        data=np.loadtxt(filename)
        return data   

          
class postprocess(inputData):
    def __init__(self,config):
        inputDataRandI.__init__(self,config)
        print "postprocess module is initionized"
        

class visualize(inputData):
    def __init__(self,config):
        inputData.__init__(self,config)
        print "Visual module is initionizied"




    #plot 
    #spiral wave
    
    def plotSpiralWaveForThesis(self,t,label=''): 
        plt.clf()
        data=self.inputSpiralWave(t)
        plt.contourf(data)       
        plt.clim(-60,40)
        plt.xlabel('Network Column Index',fontsize=fsize)
        plt.ylabel('Network Row Index',fontsize=fsize)
        cbar=plt.colorbar()
        if label!='':
            plt.title(label,fontsize=fsize)
        pathOut=os.path.join(Thesis,self.composition)
        if os.path.exists(pathOut):
            pass
        else:
            os.makedirs(pathOut)    
        plt.savefig(os.path.join(pathOut,u'%s_t=%.5f_SpiralWave.tiff'%(self.coupleAndNoise,t)))
        del cbar
     
    def plotSpiralWaves(self,listoftime=time_array):
        plt.clf()
        filter_array=time_array[-25:]#filter(lambda x:int(x)>4500,time_array)    
        for t in filter_array:
            data=self.inputSpiralWave(t)
            fig.clear()
            
            plt.contourf(data)
            plt.clim(-60,40)
            cbar=plt.colorbar()

            plt.title(u'%s_t=%.5f'%(self.plot_title,t))

            if os.path.exists(self.Visualdirect):
                pass
            else:
                os.makedirs(self.Visualdirect)
            plt.savefig(os.path.join(self.Visualdirect,u'%s_t=%.5f.%s'%(self.coupleAndNoise,t,format)))
            del cbar

    
    def plotHeterSpiralWavesForThesis(self):
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        
        for pML1 in aML1:       
            self.setProp(percML1)
            self.saveSpiralWaveForThesis(dictTimeOfDifferentPropOnlyForThesis[self.pML1],dictLabelOfDifferentProp[self.pML1])
    
    def plotThesisHeterSpiralWaves(self):
        self.setISpan(0.0)
        self.setGc(0.25)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        aText=['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)','(k)','(l)','(m)','(n)','(o)','(p)','(q)','(r)','(s)','(t)',\
        '(u)','(v)','(w)','(x)','(y)','(z)']
        for i,pML1 in enumerate(aML1):
            self.setProp(pML1)
            self.saveSpiralWaveForThesis(dictHeterSpiralWave_0_25[pML1],aText[i])       
  
    #timeseries    

     
         
    def plotTimeSeries(self):
        if self.pML1==0 or self.pML1==100:
             self.plotHomoTimeSeries()
        else:
             self.plotHeterTimeSeries()      
    
    def plotHomoTimeSeries(self):
        data=self.inputTimeSeries()  
        column=np.size(data[0][:])
        index=range(1,column)
        plt.clf()

        plt.plot(data[20000:50000,0],data[20000:50000,1],linewidth=2,color='black')
#        plt.plot(data[:,0],data[:,column])
#        plt.title(self.plot_title)
        if self.pML1==0:
            plt.ylabel(u'type II voltage(mV)',fontsize=fsize)
        else:
            plt.ylabel(u'type I voltage(mV)',fontsize=fsize)
        plt.xlabel(u'time(ms)',fontsize=fsize)
        if os.path.exists(self.Outdirect):
            pass
        else:
            os.makedirs(self.Outdirect)
        plt.savefig(os.path.join(self.Outdirect,u'%s_TimeSeries.tiff'%(self.coupleAndNoise)))
        
    def plotHeterTimeSeries(self):
        data=self.inputTimeSeries()
#        print data
        column=np.size(data[0,:])
        plt.clf()
        plt.subplot(211)
        plt.plot(data[20000:,0],data[20000:,1],linewidth=2,color='black')
        plt.title(self.plot_title)
        plt.ylabel(u'type I voltage(mV)',fontsize=fsize)
        plt.subplot(212)
        plt.plot(data[20000:,0],data[20000:,column/2+1],linewidth=2,color='black')
        plt.ylabel(u'type II voltage(mV)',fontsize=fsize)
        plt.xlabel(u'time(ms)',fontsize=fsize)
    
#        plt.title(self.plot_title)
        if os.path.exists(self.Visualdirect):
            pass
        else:
            os.makedirs(self.Visualdirect)
        plt.savefig(os.path.join(self.Visualdirect,u'%s_TimeSeries.png'%(self.coupleAndNoise)))

    def plotHeterTimeAndCoupleSeries(self):
            data=self.inputTimeSeries()
            coupleSeries=self.inputCoupleSeries()
    #        print data
            column=np.size(data[0,:])
            fig=plt.figure()
            fig.clear()
            plt.subplot(211)
            plt.title(self.plot_title)
            plt.plot(data[20000:,0],data[20000:,1],'-',linewidth=2,color='black')
            plt.plot(coupleSeries[20000:,0],coupleSeries[20000:,1],'--',linewidth=2,color='black')
            plt.ylabel(u'Type I',fontsize=fsize)
            plt.title(self.plot_title)
            plt.subplot(212)
            plt.plot(data[20000:,0],data[20000:,column/2+1],'-',linewidth=2,color='black')
            plt.plot(coupleSeries[20000:,0],coupleSeries[20000:,column/2+1],'--',linewidth=2,color='black')
            plt.ylabel(u'Type II',fontsize=fsize)
            plt.xlabel(u'time(ms)',fontsize=fsize)
                        
            if os.path.exists(self.Visualdirect):
                pass
            else:
                os.makedirs(self.Visualdirect)
            plt.savefig(os.path.join(self.Visualdirect,u'%s_TimeSeries.png'%(self.coupleAndNoise)))
    
  #animation       
    def contourGif(self):
 #       time_array=np.linspace(2020,4980,149)
 #       if self.pML1>95:
 #           time_array=np.linspace(5020,7980,149)
        duration=6
        size=len(time_array)
        fig=plt.figure()
        # DRAW A FIGURE WITH MATPLOTLIB
        def make_frame(t):
            plt.clf()
            
            
            im = plt.contourf(data[int(t*size/duration)])
            plt.clim(-60,40)
            plt.colorbar()
            def setvisible(self,vis):
                for c in self.collections: c.set_visible(vis)
            im.set_visible = types.MethodType(setvisible,im)
            im.axes = plt.gca()
            
            
            plt.title(self.plot_title)
            return mplfig_to_npimage(fig)
        #for couple in [0.24,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3]:#[0.65,0.7,0.75,0.8,0.85]:#[0.24,0.25,0.255,0.26,0.265,0.27,0.275]:
        #    for noise in [0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]:#[0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.01,0.02,0.05,0.07,0.1,0.2,0.5,0.7,1,2,5,7]:#[0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]:
        data=[]
        for time in time_array:
            d=self.inputSpiralWave(time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation =mpy.VideoClip(make_frame, duration=duration)
        plt.title(self.plot_title)
        if os.path.exists(self.Visualdirect):
            pass
        else:
            os.makedirs(self.Visualdirect)
        
        animation.write_gif(os.path.join(self.Visualdirect,u'%s.gif'%(self.coupleAndNoise)), fps=20)
    
    def contourGif_1(self,begin,end,interval):
        num=(end-begin)/interval+1
        print num
        time_array=np.linspace(begin,end,num)
        duration=6
        size=len(time_array)
        fig=plt.figure()
        # DRAW A FIGURE WITH MATPLOTLIB
        def make_frame(t):
            plt.clf()
            
            
            im = plt.contourf(data[int(t*size/duration)])
            plt.clim(-60,40)
            plt.colorbar()
            def setvisible(self,vis):
                for c in self.collections: c.set_visible(vis)
            im.set_visible = types.MethodType(setvisible,im)
            im.axes = plt.gca()
            
            
            plt.title(self.plot_title)
            return mplfig_to_npimage(fig)
        #for couple in [0.24,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3]:#[0.65,0.7,0.75,0.8,0.85]:#[0.24,0.25,0.255,0.26,0.265,0.27,0.275]:
        #    for noise in [0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]:#[0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.01,0.02,0.05,0.07,0.1,0.2,0.5,0.7,1,2,5,7]:#[0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]:
        data=[]
        for time in time_array:
            d=self.inputSpiralWave(time)
            data.append(d)
        # ANIMATE WITH MOVIEPY (UPDATE THE CURVE FOR EACH t). MAKE A GIF.
        animation =mpy.VideoClip(make_frame, duration=duration)
        plt.title(self.plot_title)
        if os.path.exists(self.Outdirect):
            pass
        else:
            os.makedirs(self.Outdirect)
        
        animation.write_gif(os.path.join(self.Outdirect,u'%s.gif'%(self.coupleAndNoise)), fps=20)
            

    
    #Autocorrelation 
    def plotACListWithFirstPeak(self):  
        data=self.inputAutoCorrelationAverage()     
        listAC=makeACList(data)
        a=range(100)#[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        Out=[]
        Out.append(a)
        Out.append(listAC)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        np.savetxt(os.path.join(self.PPdirect,u'%s_SNRList.dat'%(self.coupleAndNoise)),dataOut)
        result=firstPeakAC(listAC)        
        fig=plt.figure()
        fig.clear()
        if type(result)==tuple:
            plt.plot(a,listAC)
            
            plt.scatter(result[1],listAC[result[1]])
            plt.scatter(result[2],listAC[result[2]])
            plt.scatter(result[3],listAC[result[3]])
            plt.title(self.plot_title)
            plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRList.png'%(self.gc_exc,self.i_span)))         
        else:
            plt.plot(a,listAC)
            plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRList.png'%(self.gc_exc,self.i_span)))

           
    def plotACListWithMaximum(self,data):       
        data=self.inputAutoCorrelationAverage()  
        listAC=makeACList(data)
        list_size=len(listAC)
        a=range(0,100)

        result=MaximumLeftAndRightMinimum(listAC)
        fig=plt.figure()
        fig.clear()
        if type(result)==tuple:
            plt.plot(a,listAC)
            
            plt.scatter(result[0],listAC[result[0]])
            plt.scatter(result[1],listAC[result[1]])
            plt.scatter(result[2],listAC[result[2]])
            plt.title(self.plot_title)
            plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRList.png'%(self.gc_exc,self.i_span)))        
        else:
            plt.plot(a,listAC)
            plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRList.png'%(self.gc_exc,self.i_span)))

# population firing rate
    def plotHomoFiringRate(self,aGc_ce,format='tiff'):
        self.updateDirect()
        quant=[]
        plt.clf()
        homo=[100,0]
        labels=['Type II','Type I']
        for i,percML2 in enumerate(homo):
            ML2=int(16384.0*percML2/100.0+0.5)
            ML1=16384-ML2
            self.setProp(ML1,ML2,0,0)
            quant=[]
            for gc_ce in aGc_ce:
                self.setGc(gc_ce,gc_ce)
                
                data=self.inputAverISI()
                if len(data)==0:
                    quant.append(0)
                else:
                    quant.append(1000.0*np.mean(np.reciprocal(data)))
           
            plt.plot(aGc_ce,quant,plotCharacter[i],label=labels[i])
        plt.legend(loc='best')
        plt.xlabel(u'$g_s$$(mS/cm^2)$',fontsize=15)
        plt.ylabel(r'$f$',fontsize=15)
        
        plt.title(self.plot_title)
        if os.path.exists(self.Outdirect):
            pass
        else:
            os.makedirs(self.Outdirect)
        plt.savefig(os.path.join(self.Outdirect,u'%s_Homo_FiringRate.%s'%(self.coupleAndNoise,format)))
        
    def plotHeterFiringRate(self,aGc_ce):
        quant=[]
        plt.clf()
        for i,gc_ce in enumerate(aGc_ce):
            self.setGc(gc_ce)
            quant=[]
            for pML1 in aML1:
                self.setProp(pML1)
                data=self.inputAverISI()
                quant.append(1000.0*np.mean(np.reciprocal(data)))
            plt.plot(aML1,quant,label=r'$g_s =$ $%.2f$'%gc_ce,markersize=12)
#        plt.title('(a)')
        plt.legend(loc='best')
       
#        plt.title(self.coupleAndNoise)
#        plt.xlabel(u'Percentage of Type I Neurons(%)')
#        plt.ylabel(u'Population Firing Rate(Hz)')
        plt.xlabel(r'$p ( \% ) $',fontsize=15)
        plt.ylabel(r'$f$',fontsize=15)
        if os.path.exists(self.Visual):
            pass
        else:
            os.makedirs(self.Visual)
        plt.savefig(os.path.join(self.Visual,u'Heter_FiringRate.png'))  
        
    def plotHeterFiringRateForOneAndTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        fig=plt.figure()
        fig.clear()
        aFreType1=[]
        aFreStdType1=[]
        aFreType2=[]
        aFreStdType2=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputAverISI()
            aFreList=1000.0*np.reciprocal(data)
            aMax.append(np.max(aFreList))
            aMin.append(np.min(aFreList))
            data1=self.inputAverISIType1()
            freListType1=1000.0*np.reciprocal(data1)
            data2=self.inputAverISIType2()
            freListType2=1000.0*np.reciprocal(data2)
            aFreType1.append(np.mean(freListType1))
            aFreStdType1.append(np.std(freListType1))
            aFreType2.append(np.mean(freListType2))
            aFreStdType2.append(np.std(freListType2))
        plt.subplot(211)
        plt.title('g=%.5f'%(self.gc_exc))
        plt.plot(aML1,aFreType1,'-')
        plt.plot(aML1,aFreType2,'--')
        plt.ylabel('mean of frequency')
        plt.subplot(212)
        plt.plot(aML1,aFreStdType1,'-')
        plt.plot(aML1,aFreStdType2,'--')
        plt.ylabel('std of frequency')
        plt.xlabel('p(%)')        
        filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_HeterFiringRateForOneAndTwo.png'%(self.i_span,self.gc_exc))
        plt.savefig(filename)   
    def plotHeterISIForOneAndTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        fig=plt.figure()
        fig.clear()
        aISIType1=[]
        aISIStdType1=[]
        aISIType2=[]
        aISIStdType2=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            data1=self.inputAverISIType1()
            isiListType1=data1
            data2=self.inputAverISIType2()
            isiListType2=data2
            aISIType1.append(np.mean(isiListType1))
            aISIStdType1.append(np.std(isiListType1))
            aISIType2.append(np.mean(isiListType2))
            aISIStdType2.append(np.std(isiListType2))
        plt.subplot(211)
        plt.title('g=%.5f'%(self.gc_exc))
        plt.plot(aML1,aISIType1,'-')
        plt.plot(aML1,aISIType2,'--')
        plt.ylabel('mean of isi')
        plt.subplot(212)
        plt.plot(aML1,aISIStdType1,'-')
        plt.plot(aML1,aISIStdType2,'--')
        plt.ylabel('std of isi')
        plt.xlabel('p(%)')        
#        filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_HeterFiringRateForOneAndTwo.png'%(self.i_span,self.gc_exc))
        filename=os.path.join('C:\\users\\shaw\\desktop\\visual1',u'i_span=%.5f_gc=%.5f_HeterISIForOneAndTwo.png'%(self.i_span,self.gc_exc))
        plt.savefig(filename)  
                         
    def plotHeterISIAndCVForOneAndTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        fig=plt.figure()
        fig.clear()
        aMaxISIType1=[]
        aMinISIType1=[]
        aAverISIType1=[]
        aMaxCVType1=[]
        aMinCVType1=[]
        aAverCVType1=[]
#        aCVStdType1=[]
        aMaxISIType2=[]
        aMinISIType2=[]
        aAverISIType2=[]
        aMaxCVType2=[]
        aMinCVType2=[]
        aAverCVType2=[]
#        aCVStdType2=[]

        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            isiListType1=self.inputAverISIType1()
            isiListType2=self.inputAverISIType2()
            cvListType1=self.inputCVType1()
            cvListType2=self.inputCVType2()
            
            maxIDType1=maximumIndex(isiListType1)
            minIDType1=minimumIndex(isiListType1)
            maxIDType2=maximumIndex(isiListType2)
            minIDType2=minimumIndex(isiListType2)
            
            aMaxISIType1.append(isiListType1[maxIDType1])
            aMinISIType1.append(isiListType1[minIDType1])
#            aAverISIType1.append(np.mean(isiListType1))
            aMaxCVType1.append(cvListType1[maxIDType1])
            aMinCVType1.append(cvListType1[minIDType1])
#            aAverCVType1.append(np.mean(cvListType1))
            
            aMaxISIType2.append(isiListType2[maxIDType2])
            aMinISIType2.append(isiListType2[minIDType2])
#            aAverISIType2.append(np.mean(isiListType2))
            aMaxCVType2.append(cvListType2[maxIDType2])
            aMinCVType2.append(cvListType2[minIDType2])
#            aAverCVType2.append(np.mean(cvListType2))
            

        plt.title('g=%.5f'%(self.gc_exc))
        plt.subplot(221)
        plt.title('Type I')
        plt.plot(aML1,aMaxISIType1,'-')
        plt.plot(aML1,aMinISIType1,'--')
        plt.ylim([50,90])
        plt.ylabel('ISI')
        plt.subplot(223)
        plt.plot(aML1,aMaxCVType1,'-')
        plt.plot(aML1,aMinCVType1,'--')
        plt.ylim([0,0.25])
        plt.ylabel('CV')
        plt.xlabel('p(%)')
        
        plt.subplot(222)
        plt.title('Type II')
        plt.plot(aML1,aMaxISIType2,'-')
        plt.plot(aML1,aMinISIType2,'--')
        plt.ylim([50,90])
        plt.subplot(224)
        plt.plot(aML1,aMaxCVType2,'-')
        plt.plot(aML1,aMinCVType2,'--')
        plt.ylim([0,0.25])
        plt.xlabel('p(%)')
        
        filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_HeterCVAndISIForOneAndTwo.png'%(self.i_span,self.gc_exc))
        plt.savefig(filename)  
        
    def plotHeterCVForOneAndTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        fig=plt.figure()
        fig.clear()
        aCVType1=[]
        aCVStdType1=[]
        aCVType2=[]
        aCVStdType2=[]
        aMax=[]
        aMin=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            cvListType1=self.inputCVType1()
            cvListType2=self.inputCVType2()
            aCVType1.append(np.mean(cvListType1))
            aCVStdType1.append(np.std(cvListType1))
            aCVType2.append(np.mean(cvListType2))
            aCVStdType2.append(np.std(cvListType2))
#        plt.subplot(311)
#        plt.plot(aML1,aMax,'-')
#        plt.plot(aML1,aMin,'--')
#        plt.ylabel('max and min')
        plt.subplot(211)
        plt.title('g=%.5f'%(self.gc_exc))
        plt.plot(aML1,aCVType1,'-')
        plt.plot(aML1,aCVType2,'--')
        plt.ylabel('mean of CV')
        plt.subplot(212)
        plt.plot(aML1,aCVStdType1,'-')
        plt.plot(aML1,aCVStdType2,'--')
        plt.ylabel('std of CV')
        plt.xlabel('p(%)')
        
#        filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_HeterCVForOneAndTwo.png'%(self.i_span,self.gc_exc))
        filename=os.path.join('C:\\users\\shaw\\desktop\\visual1',u'i_span=%.5f_gc=%.5f_HeterCVForOneAndTwo.png'%(self.i_span,self.gc_exc))
        plt.savefig(filename)

    def plotISIToCVForOneAndTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            plt.clf()
            self.setProp(pML1)
            isiListType1=self.inputAverISIType1()
            isiListType2=self.inputAverISIType2()
            cvListType1=self.inputCVType1()
            cvListType2=self.inputCVType2()
            plt.subplot(211)
            plt.scatter(isiListType1,cvListType1)
            xmin1,xmax1=plt.xlim()[0],plt.xlim()[1]
            ymin1,ymax1=plt.ylim()[0],plt.ylim()[1]
            plt.subplot(212)
            plt.scatter(isiListType2,cvListType2)
            xmin2,xmax2=plt.xlim()[0],plt.xlim()[1]
            ymin2,ymax2=plt.ylim()[0],plt.ylim()[1]
            xmin=min(xmin1,xmin2)
            xmax=max(xmax1,xmax2)
            ymin=min(ymin1,ymin2)
            ymax=max(ymax1,ymax2)
            plt.subplot(211)
            plt.xlim([xmin,xmax])
            plt.ylim([ymin,ymax])
            plt.ylabel(u'coherence variation')
            plt.title('ML1=%d%%'%(self.pML1))
            plt.subplot(212)
            plt.xlim([xmin,xmax])
            plt.ylim([ymin,ymax])
            plt.xlabel(u'interspike interval')
            plt.ylabel(u'coherence variation')
            if os.path.exists(self.Visualdirect):
                pass
            else:
                os.makedirs(self.Visualdirect)
                
            filename=os.path.join(self.Visualdirect,u'i_span=%.5f_gc=%.5f_CVToISIForOneAndTwo.png'%(self.i_span,self.gc_exc))
            plt.savefig(filename)  
            
                        
    def plotHeterISIAndCVForOnePlusTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        fig=plt.figure()
        fig.clear()
        aMaxISIType1=[]
        aMinISIType1=[]
        aAverISIType1=[]
        aMaxCVType1=[]
        aMinCVType1=[]
        aAverCVType1=[]
#        aCVStdType1=[]
        aMaxISIType2=[]
        aMinISIType2=[]
        aAverISIType2=[]
        aMaxCVType2=[]
        aMinCVType2=[]
        aAverCVType2=[]
#        aCVStdType2=[]

        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            isiListType1=self.inputAverISIType1()
            isiListType2=self.inputAverISIType2()
            cvListType1=self.inputCVType1()
            cvListType2=self.inputCVType2()
            
            maxIDType1=maximumIndex(isiListType1)
            minIDType1=minimumIndex(isiListType1)
            maxIDType2=maximumIndex(isiListType2)
            minIDType2=minimumIndex(isiListType2)
            
            aMaxISIType1.append(isiListType1[maxIDType1])
            aMinISIType1.append(isiListType1[minIDType1])
#            aAverISIType1.append(np.mean(isiListType1))
            aMaxCVType1.append(cvListType1[maxIDType1])
            aMinCVType1.append(cvListType1[minIDType1])
#            aAverCVType1.append(np.mean(cvListType1[cvListType1]))
            
            aMaxISIType2.append(isiListType2[maxIDType2])
            aMinISIType2.append(isiListType2[minIDType2])
#            aAverISIType2.append(np.mean(isiListType2))
            aMaxCVType2.append(cvListType2[maxIDType2])
            aMinCVType2.append(cvListType2[minIDType2])
#            aAverCVType2.append(np.mean(cvListType2))
            

        plt.title('g=%.5f'%(self.gc_exc))
        plt.subplot(211)
        plt.title('Type I(blue) And Type II(red)')
        plt.plot(aML1,aMaxISIType1,'b-')
        plt.plot(aML1,aMinISIType1,'b--')
        plt.plot(aML1,aMaxISIType2,'r-')
        plt.plot(aML1,aMinISIType2,'r--')
        plt.ylabel('ISI')
    
#        plt.ylim([50,90])
#        plt.ylabel('ISI')
        plt.subplot(212)
        plt.ylabel('CV')
        plt.plot(aML1,aMaxCVType1,'b-')
        plt.plot(aML1,aMinCVType1,'b--')
        plt.plot(aML1,aMaxCVType2,'r-')
        plt.plot(aML1,aMinCVType2,'r--')
#        plt.ylabel('CV')
        plt.xlabel('p(%)')
        
#        filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_HeterCVAndISIForOnePlusTwo.png'%(self.i_span,self.gc_exc))
        filename=os.path.join('C:\\users\\shaw\\desktop\\visual1',u'i_span=%.5f_gc=%.5f_HeterCVAndISIForOnePlusTwo.png'%(self.i_span,self.gc_exc))
        plt.savefig(filename)  
                         
    def plotHistISIForOneAndTwo(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        MinML1=BeginForGc[gc]
        MaxML1=EndForGc[gc]
        for pML1 in aML1:
            plt.clf()
            # fig.clear()
            self.setProp(pML1)
            data1=self.inputAverISIType1()
            data2=self.inputAverISIType2()
            plt.subplot(211)
            #if pML1<MinML1:
            #    s='Synchronous State or regular waves'
            #elif pML1>MaxML1:
            #    s='random-like waves'
            #else:
            #    s='spiral waves'
            plt.title('ML1=%d%%'%(self.pML1))
            plt.hist(data1,bins=100)
            plt.ylabel('Type I')
            x1l=plt.xlim()[0]
            x1b=plt.xlim()[1]
#            x1=(plt.xlim()[0]+2.0*plt.xlim()[1])/3.0
            y1=(plt.ylim()[0]+4.0*plt.ylim()[1])/5.0
            
           # plt.xlim([60,90])
            
            plt.subplot(212)
            plt.hist(data2,bins=100)
            plt.ylabel('Type II')
            plt.xlabel('ISI')
            x2l=plt.xlim()[0]
            x2b=plt.xlim()[1]
#            x2=(plt.xlim()[0]+2.0*plt.xlim()[1])/3.0
            y2=(plt.ylim()[0]+4.0*plt.ylim()[1])/5.0
            xl=min([x1l,x2l,x1b,x2b])
            xb=max([x1l,x2l,x1b,x2b])
            x=(xl+2.0*xb)/3.0
            plt.subplot(211)
            plt.xlim([xl,xb])
        #    plt.yscale('log')
            plt.text(x,y1,'Aver=%.5f_Std=%.5f'%(np.mean(data1),np.std(data1)))
            plt.subplot(212)
            plt.xlim([xl,xb])
         #   plt.yscale('log')
            plt.text(x,y2,'Aver=%.5f_Std=%.5f'%(np.mean(data2),np.std(data2)))
            if os.path.exists(self.Visualdirect):
                pass
            else:
                os.makedirs(self.Visualdirect)
                
            filename=os.path.join(self.Visualdirect,u'i_span=%.5f_gc=%.5f_HistISIForOneAndTwo.png'%(self.i_span,self.gc_exc))
            plt.savefig(filename)  
     
    def plotHistCVForOneAndTwo(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        MinML1=BeginForGc[gc]
        MaxML1=EndForGc[gc]
        for pML1 in aML1:
            plt.clf()
            # fig.clear()
            self.setProp(pML1)
            data1=self.inputCVType1()
            data2=self.inputCVType2()
            plt.subplot(211)

            plt.title('g=%.5f_ML1=%d%%_%s'%(self.gc_exc,self.pML1,s))
            plt.hist(data1,bins=100)
            plt.ylabel('Type I')
            x1l=plt.xlim()[0]
            x1b=plt.xlim()[1]
            y1=(plt.ylim()[0]+4.0*plt.ylim()[1])/5.0

            plt.subplot(212)
            plt.hist(data2,bins=100)
            plt.ylabel('Type II')
            plt.xlabel('CV')
            x2l=plt.xlim()[0]
            x2b=plt.xlim()[1]
            y2=(plt.ylim()[0]+4.0*plt.ylim()[1])/5.0
            
            xl=min([x1l,x2l,x1b,x2b])
            xb=max([x1l,x2l,x1b,x2b])
            x=(xl+2.0*xb)/3.0
            plt.subplot(211)
            plt.xlim([xl,xb])
            plt.text(x,y1,'Aver=%.5f_Std=%.5f'%(np.mean(data1),np.std(data1)))
            plt.subplot(212)
            plt.xlim([xl,xb])
            plt.text(x,y2,'Aver=%.5f_Std=%.5f'%(np.mean(data2),np.std(data2)))
            
            
     #       filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_ML1_%d_HIST_CV.png'%(self.i_span,self.gc_exc,self.pML1))
            filename=os.path.join('C:\\users\\shaw\\desktop\\visual1',u'i_span=%.5f_gc=%.5f_ML1_%d_HIST_CV.png'%(self.i_span,self.gc_exc,self.pML1))
            plt.savefig(filename)
    def plotHeterCoupleAverForOneAndTwo(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]        
        aCoupleType1=[]
        aCoupleType2=[]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputCoupleSeries()
            column=np.size(data[0,:])
            aToAverType1=[]
            aToAverType2=[]
            for i in range(1,column/2+1):
                aToAverType1.append(np.mean(data[:,i]))
            aCoupleType1.append(np.mean(aToAverType1))
            
            for i in range(column/2+1,column):
                aToAverType2.append(np.mean(data[:,i]))
            aCoupleType2.append(np.mean(aToAverType2))
            
        plt.clf()
        plt.plot(aML1,aCoupleType1,'-')
        plt.plot(aML1,aCoupleType2,'--')
        plt.title(self.plot_title)
        plt.xlabel('p(%)')
        plt.savefig(os.path.join(Visual,u'i_span=%.5f_gc=%.5f_ML1=%d_HeterCoupleAver.png'%(self.i_span,self.gc_exc,self.pML1)))
    
    def plotISIAndCVAndCoupling(self,gc,i_span): 
        self.setGc(gc)
        self.setISpan(i_span)
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_ML1=1_ISIAndCVAndCoupling.txt'%(self.i_span,self.gc_exc))
        if not os.path.isfile(filename):
            print 'file not found!'
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        
        aISIType1=[]
        aCVType1=[]
        aCSMaxType1=[]
        aCSAverType1=[]
        aISIType2=[]
        aCVType2=[]
        aCSMaxType2=[]
        aCSAverType2=[]
        
        MinML1=BeginForGc[gc]
        MaxML1=EndForGc[gc]
        
        for pML1 in aML1:
            config='F:\\config\\ML1=%d_NO.dat'%(pML1)
            NoMatrix=np.loadtxt(config)
       #     row=np.size(NoMatrix[:,0])
            column=np.size(NoMatrix[0,:])
            self.setProp(pML1)
            isiAll=self.inputAverISI()
            cvAll=self.inputCV()
            coupling=self.inputCoupleSeries()
            
            isiType1=self.inputAverISIType1()            
            averISIType1=np.mean(isiType1)
            nType1=NoMatrix[0,0]
            indexType1=0
            minDiff=abs(isiAll[nType1]-averISIType1)
            for i,n in enumerate(NoMatrix[0,:]):
                if minDiff>abs(isiAll[int(n)]-averISIType1):
                    nType1=int(n)
                    minDiff=abs(isiAll[int(n)]-averISIType1)
                    indexType1=i
                    
            aISIType1.append(isiAll[nType1])
            aCVType1.append(cvAll[nType1])
            aCSMaxType1.append(max(coupling[:,indexType1+1]))
            aCSAverType1.append(np.mean(coupling[:,indexType1+1]))
            
            isiType2=self.inputAverISIType2()
            averISIType2=np.mean(isiType2)
            nType2=NoMatrix[1,0]
            indexType2=0
            minDiff=abs(isiAll[nType2]-averISIType2)
            for i,n in enumerate(NoMatrix[1,:]):
                if minDiff>abs(isiAll[int(n)]-averISIType2):
                    nType2=int(n)
                    minDiff=abs(isiAll[int(n)]-averISIType2)
                    indexType2=i
                    
            aISIType2.append(isiAll[nType2])
            aCVType2.append(cvAll[nType2])
            aCSMaxType2.append(max(coupling[:,indexType2+column+1]))
            aCSAverType2.append(np.mean(coupling[:,indexType2+column+1]))
            
            plt.clf()
            plt.plot(coupling[25000:,0],coupling[25000:,indexType1+1],'-')
            plt.plot(coupling[25000:,0],coupling[25000:,indexType2+column+1],'--')
            if pML1<MinML1:
                s='Synchronous State or regular waves'
            elif pML1>MaxML1:
                s='random-like waves'
            else:
                s='spiral waves'
            plt.title('g=%.5f_ML1=%d%%_%s'%(self.gc_exc,self.pML1,s))
#            filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_ML1=%d_CouplingSeriesForOneAndTwo.png'%(self.i_span,self.gc_exc,self.pML1))
            filename=os.path.join('C:\\users\\shaw\\desktop\\visual3',u'i_span=%.5f_gc=%.5f_ML1=%d_CouplingSeriesForOneAndTwo.png'%(self.i_span,self.gc_exc,self.pML1))
            plt.savefig(filename)
            
        plt.clf()
        plt.subplot(411)
        plt.title('g=%.5f'%(self.gc_exc))
        plt.plot(aML1,aISIType1,'-')
        plt.plot(aML1,aISIType2,'--')
        plt.ylabel('ISI')
        plt.subplot(412)
        plt.plot(aML1,aCVType1,'-')
        plt.plot(aML1,aCVType2,'--')
        plt.ylabel('CV')
        plt.subplot(413)
        plt.plot(aML1,aCSMaxType1,'-')
        plt.plot(aML1,aCSMaxType2,'--')
        plt.ylabel('CoupleMax')
        plt.subplot(414)
        plt.plot(aML1,aCSAverType1,'-')
        plt.plot(aML1,aCSAverType2,'--')
        plt.ylabel('CoupleAver')
        plt.xlabel('p(%)')
#        filename=os.path.join(Visual,u'i_span=%.5f_gc=%.5f_ISI_CV_Coupling.png'%(self.i_span,self.gc_exc))
        filename=os.path.join('C:\\users\\shaw\\desktop\\visual3',u'i_span=%.5f_gc=%.5f_ISI_CV_Coupling.png'%(self.i_span,self.gc_exc))
        plt.savefig(filename)    

    #phase order                             
    def plotHomoPhaseOrder(self,aGc_ce,format='tiff'):
        quant=[]
        fig=plt.figure()
        fig.clear()
        saveML1=self.ml1
        saveML2=self.ml2
        saveGc_exc=self.gc_exc
        saveGc_inh=self.gc_inh

        homo=[100,0]
        for percML2 in homo:
            ML2=int(16384.0*percML2/100.0+0.5)
            ML1=16384-ML2
            self.setProp(ML1,ML2,0,0)
            quant=[]
            for gc_ce in aGc_ce:
                self.setGc(gc_ce,gc_ce)
                
                data=self.inputPhaseAmplitude()
                quant.append(np.mean(data))
            if percML2==100:
                plt.plot(aGc_ce,quant,label=u'Type II')
            if percML2==0:
                plt.plot(aGc_ce,quant,label=u'Type I')
#        plt.title('(a)')
        plt.legend(loc='best')
            
#        plt.title(self.coupleAndNoise)
        plt.xlabel(u'$g _s$ $(mS/cm^2)$',fontsize=15)
#        plt.ylabel(u'Phase Order Parameter')
        plt.ylabel(r'$R$',fontsize=15)
        if os.path.exists(self.Outdirect):
            pass
        else:
            os.makedirs(self.Outdirect)
        plt.savefig(os.path.join(self.Outdirect,u'RandI(%.5f,%.5f)_Homo_PhaseOrder.%s'%(self.i_span,format)))
        self.setProp(saveML1,saveML2,0,0)
        self.setGc(saveGc_exc,saveGc_inh)
 
    def plotHeterPhaseOrder(self,aGc_ce):
        quant=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        plt.clf()
        for i,gc_ce in enumerate(aGc_ce):
            self.setGc(gc_ce)
            quant=[]
            for pML1 in aML1:
                self.setProp(pML1)
                data=self.inputPhaseAmplitude()
                quant.append(np.mean(data))
            plt.plot(aML1,quant,label=r'$g_s =$ $%.2f$'%(self.gc_exc),markersize=12)
#        plt.title('(b)')
        plt.legend(loc='best')   
        plt.xlabel(r'$p ( \% ) $',fontsize=15)
        plt.ylabel(r'$R$',fontsize=15)
        if os.path.exists(self.Visual):
            pass
        else:
            os.makedirs(self.Visual)
        plt.savefig(os.path.join(self.Visual,u'Heter_PhaseOrder.png'))
    

                        
            
# save txt
    def saveHomoPhaseOrder(self,aGc,i_span):        

        aQI1=[]
        aQI2=[]
        self.setISpan(i_span)
        self.setProp(100)
        for gc in aGc:
            self.setGc(gc)
            data=self.inputPhaseAmplitude()
            aQI1.append(np.mean(data))
        
        self.setProp(0)
        for gc in aGc:
            self.setGc(gc)
            data=self.inputPhaseAmplitude()
            aQI2.append(np.mean(data))
        Out=[]  
        Out.append(aGc)
        Out.append(aQI1)
        Out.append(aQI2)
        dataOut=np.array(Out)
        dataOut.tranpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HomoPhaseOrder.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,data)

            
    def saveHeterPhaseOrder(self,gc,i_span):  
        self.setGc(gc)
        self.setISpan(i_span)      
        aQI=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputPhaseAmplitude()
            aQI.append(np.mean(data))
        Out=[]
        Out.append(aML1)
        Out.append(aQI)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterPhaseOrder.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,dataOut)

    def savePoints(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        a=range(0,100)
        Out=[]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputAutoCorrelationAverage()
            listAC=makeACList(data)
            result=MaximumLeftAndRightMinimum(listAC)
            fig=plt.figure()
            fig.clear()
            if type(result)==tuple:
                Out.append([pML1,result[0],result[1],result[2]])
                plt.plot(a,listAC)
            
                plt.scatter(result[0],listAC[result[0]])
                plt.scatter(result[2],listAC[result[2]])
                plt.scatter(result[1],listAC[result[1]])
                plt.title(self.plot_title)
                plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRList.png'%(self.gc_exc,self.i_span)))
            else:
                plt.plot(a,listAC)
                plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRList.png'%(self.gc_exc,self.i_span)))
                Out.append([pML1,99,99,99])
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterPoints.txt'%(self.i_span,self.gc_exc))    
        dataOut=np.array(Out)
        np.savetxt(filename,dataOut)
            
    def saveDeltaQAndQMaxFromPointsRevised(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        
        Out=[]
        DeltaQ=[]
        QMax=[]
        Out.append(aML1)
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterPointsRevised.dat'%(self.i_span,self.gc_exc))    
        points=np.loadtxt(filename)
        a1=range(0,100)
        for i,pML1 in enumerate(aML1):
            self.setProp(pML1)
            data=self.inputAutoCorrelationAverage()
            ACList=makeACList(data)
            fig=plt.figure()
            fig.clear()
            plt.plot(a1,ACList)
            plt.scatter(points[i,3],ACList[int(points[i,3])])
            plt.scatter(points[i,2],ACList[int(points[i,2])])
            plt.scatter(points[i,1],ACList[int(points[i,1])])
            plt.title(self.plot_title)
            plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRListFromPoints.png'%(self.gc_exc,self.i_span)))
            if points[i,1]==99:
                DeltaQ.append(0)
                QMax.append(ACList[-1])
            else:
                d1=2.0*ACList[int(points[i,2])]-ACList[int(points[i,1])]-ACList[int(points[i,3])];
                d2=points[i,3]-points[i,1];
                delta=d1/d2;
                DeltaQ.append(delta)
                maxq=ACList[int(points[i,2])]
                QMax.append(maxq)
                
        Out.append(DeltaQ)
        Out.append(QMax)
        
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterDeltaQAndQMax.txt'%(self.i_span,self.gc_exc))   
        np.savetxt(filename,dataOut)
        
    def saveDeltaQAndQMaxFromPointsRaw(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        
        Out=[]
        DeltaQ=[]
        QMax=[]
        Out.append(aML1)
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterPoints.txt'%(self.i_span,self.gc_exc))    
        points=np.loadtxt(filename)
        a1=range(0,100)
        for i,pML1 in enumerate(aML1):
            self.setProp(pML1)
            data=self.inputAutoCorrelationAverage()
            ACList=makeACList(data)
            fig=plt.figure()
            fig.clear()
            plt.plot(a1,ACList)
            plt.scatter(points[i,3],ACList[int(points[i,3])])
            plt.scatter(points[i,2],ACList[int(points[i,2])])
            plt.scatter(points[i,1],ACList[int(points[i,1])])
            plt.title(self.plot_title)
            plt.savefig(os.path.join(self.Visualdirect,u'gc=%.5f_i_span=%.5f_SNRListFromPointsRaw.png'%(self.gc_exc,self.i_span)))
            if points[i,1]==99:
                DeltaQ.append(0)
                QMax.append(ACList[-1])
            else:
                d1=2.0*ACList[int(points[i,2])]-ACList[int(points[i,1])]-ACList[int(points[i,3])];
                d2=points[i,3]-points[i,1];
                delta=d1/d2;
                DeltaQ.append(delta)
                maxq=ACList[int(points[i,2])]
                QMax.append(maxq)
                
        Out.append(DeltaQ)
        Out.append(QMax)
        
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterDeltaQAndQMaxRaw.txt'%(self.i_span,self.gc_exc))   
        np.savetxt(filename,dataOut)            
    def saveHeterFiringRateForOneAndTwo(self,gc,i_span):        
        self.setGc(gc)
        self.setISpan(i_span)    
        aFreType1=[]
        aFreStdType1=[]
        aFreType2=[]
        aFreStdType2=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            data1=self.inputAverISIType1()
            freListType1=1000.0*np.reciprocal(data1)
            data2=self.inputAverISIType2()
            freListType2=1000.0*np.reciprocal(data2)
            aFreType1.append(np.mean(freListType1))
            aFreStdType1.append(np.std(freListType1))
            aFreType2.append(np.mean(freListType2))
            aFreStdType2.append(np.std(freListType2))
        Out=[]
        Out.append(aML1)
        Out.append(aFreType1)
        Out.append(aFreStdType1)
        Out.append(aFreType2)
        Out.append(aFreStdType2)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterFiringRateForOneAndTwo.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,dataOut) 
                    
    def saveSNRList(self,pML1,gc,i_span):

        aRadius=range(0,100)
        self.setProp(pML1)
        self.setGc(gc)
        self.setISpan(i_span)
        data=self.inputAutoCorrelationAverage()
        SNRList=makeACList(data)
        Out=[]
        Out.append(aRadius)
        Out.append(SNRList)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        filename=os.path.join(self.PP,u'i_span=%.5f_gc=%.5f_ML1=%d_SNRList.txt'%(self.i_span,self.gc_exc,self.ml1))
        np.savetxt(filename,dataOut)
 
        
    def saveHomoSNR(self,i_span):        
        saveML1=self.pML1
        saveGc_exc=self.gc_exc
        savei_span=self.i_span

        aQI1=[]
        aQI2=[]
        aGc=[]
        self.setISpan(i_span)
        self.setProp(100)
        for gc in aGc:
            self.setGc(gc)
            data=self.inputAutoCorrelationAverage()
            aQI1.append(self.AC2SNR(data))
        
        self.setProp(0)
        for gc in aGc:
            self.setGc(gc)
            data=self.inputAutoCorrelationAverage()
            aQI2.append(self.AC2SNR(data))
        Out=[]  
        Out.append(aGc)
        Out.append(aQI1)
        Out.append(aQI2)
        dataOut=np.array(Out)
        dataOut.tranpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HomoSNR.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,data)
        self.setProp(saveML1)
        self.setGc(saveGc_exc)
        self.setI_span(savei_span)
            
    def saveHeterSNR(self,gc,i_span):        

        aQI=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputAutoCorrelationAverage()
            aQI.append(self.AC2SNR(data))
        Out=[]
        Out.append(aML1)
        Out.append(aQI)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterSNR.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,dataOut)
    def saveHeterCV(self,gc,i_span):
        self.setGc(gc)
        self.setISpan(i_span)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        aTypeI=[]
        aTypeII=[]
        aTotal=[]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputCV()
            filename=os.path.join('F:\\config','ML1=%d_NO.dat'%(pML1))
            No=np.loadtxt(filename)
#            print No[0,0],int(No[0,0]),No[1,0],int(No[1,0])
            aTypeI.append(data[int(No[0,2])])
            aTypeII.append(data[int(No[1,2])])
            aTotal.append(np.mean(data))
        #    aQI.append(self.AC2SNR(data))
        Out=[]
        Out.append(aML1)
        Out.append(aTypeI)
        Out.append(aTypeII)
        Out.append(aTotal)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterCV.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,dataOut)
    def saveISIAndCVAndCoupling(self,gc,i_span,pML1):
        self.setGc(gc)
        self.setISpan(i_span)
        self.setProp(pML1)
        config='F:\\config\\ML1=%d_NO.dat'%(pML1)
        NoMatrix=np.loadtxt(config)
        row=np.size(NoMatrix[:,0])
        column=np.size(NoMatrix[0,:])
        NO=[]
        for i in range(row):
            for j in range(column):
                NO.append(int(NoMatrix[i,j]))                
        coupling=self.inputCoupleSeries()
        ISI=self.inputAverISI()
        CV=self.inputCV()
        Out=[]
        # ISI CV CS_Max CS_Aver
        for i,n in enumerate(NO):
            OneNeuron=[]
            OneNeuron.append(n)
            OneNeuron.append(ISI[n])
            OneNeuron.append(CV[n])
            OneNeuron.append(max(coupling[:,i+1]))
            OneNeuron.append(np.mean(coupling[:,i+1]))
            Out.append(OneNeuron)
        Out=np.array(Out)
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_ML1=%d_ISIAndCVAndCoupling.txt'%(self.i_span,self.gc_exc,self.pML1))
        np.savetxt(filename,Out)
            
    def saveSNR_List(self,gc,i_span):
        self.setISpan(i_span)
        self.setGc(gc)
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        aRadius=range(0,100)
        for i,ML1 in enumerate(aML1):
             self.setProp(ML1)
             data=self.inputAutoCorrelationAverage()
             SNRList=makeACList(data)
             Out=[]
             Out.append(aRadius)
             Out.append(SNRList)
             dataOut=np.array(Out)
             dataOut=dataOut.transpose()
             direct=os.path.join(PP,u'SNRList\\gc=%.5f'%(self.gc_exc))
             if os.path.exists(direct):
                pass
             else:
                os.makedirs(direct)
             filename=os.path.join(PP,u'SNRList\\gc=%.5f\\i_span=%.5f_ML1=%d_SNRList.txt'%(self.gc_exc,self.i_span,self.pML1))
             np.savetxt(filename,dataOut)
             
    def saveHomoFiringRate(self,i_span):        
        aQI1=[]
        aQI2=[]
        aGc=[]
        self.setISpan(i_span)
        self.setProp(100)
        for gc in aGc:
            self.setGc(gc)
            data=self.inputAverISI()
            aQI1.append(1000.0*np.mean(np.reciprocal(data)))
        
        self.setProp(0)
        for gc in aGc:
            self.setGc(gc)
            data=self.inputAverISI()
            aQI2.append(1000.0*np.mean(np.reciprocal(data)))
        Out=[]   
        Out.append(aGc)
        Out.append(aQI1)
        Out.append(aQI2)
        dataOut=np.array(Out)
        dataOut=dataOut.tranpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HomoFiringRate.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,data)

        
    def saveHeterFiringRate(self,gc,i_span):        
        
        self.setGc(gc)
        self.setISpan(i_span)    
        aQI=[]
        aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]
        for pML1 in aML1:
            self.setProp(pML1)
            data=self.inputAverISI()
            aQI.append(1000.0*np.mean(np.reciprocal(data)))
        Out=[]
        Out.append(aML1)
        Out.append(aQI)
        dataOut=np.array(Out)
        dataOut=dataOut.transpose()
        filename=os.path.join(PP,u'i_span=%.5f_gc=%.5f_HeterFiringRate.txt'%(self.i_span,self.gc_exc))
        np.savetxt(filename,dataOut)
        
#plot
#
if __name__=='__main__':
   aML1=[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99] 
   para=parameterExc(50,0.27,36,-25,'Sparser',p=0.1)
  # para=parameterInh(24,25,1,1,1,1,1,'Square',1)
   instance=visualize(para)
   for pML1 in aML1:
       para.setProp(pML1)
       instance.updateConfig(para)
       instance.
#       instance.contourGif()
#    instance=visualizeRandI(100,0.25,0.0)
#    instance.plotThesisHeterSpiralWaves()
#    for pML1 in [5]:#[1,99]:
#        instance.setProp(pML1)
#        instance.saveSpiralWaves()
#    instance.saveHeterTimeSeries1(0.28,0.2)
#    instance.plotThesisHeterSpiralWaves()
#    instance.setProp(99)
#    for g in [0.27]:#[0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.33]:#[0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.33,0.35]:
#        instance.plotISIToCVForOneAndTwo(g,0)
#        instance.plotHeterCoupleAverForOneAndTwo(g,0)
#        instance.plotCVtoISIForOneAndTwo(g,0)
#        instance.plotHistISIForOneAndTwo(g,0)
#        instance.plotISIAndCVAndCoupling(g,0.2)
#        for pML1 in [1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]:
#        instance.plotHeterFiringRateForOneAndTwo(g,0.2)
#             instance.saveISIAndCVAndCoupling(g,0.2,pML1)
#        instance.plotHeterISIForOneAndTwo(g,0.0)
#        instance.plotHeterCVForOneAndTwo(g,0.0)
#        instance.plotHeterISIAndCVForOneAndTwo(g,0.0)
#        instance.plotHeterISIAndCVForOnePlusTwo(g,0.0)
#        instance.plotHistISI(g,0.0)
#        instance.plotHistCV(g,0.0)
#        instance.setGc(g)
#        instance.contourGif()
#        instance.saveHeterSNR(g,0.0)
#        instance.getValuesFromPointsRevised(g,0.0)
#        instance.saveSNR_List(g,0.0)
#        instance.savePoints(g,0.0)
#        instance.getValuesFromPointsRaw(g,0.0)

#        instance.saveHeterPhaseOrder(g,0.0)
#        instance.saveHeterFiringRate(g,0.0)
#    instance.saveHeterCV(0.22,0.2)
#    instance.getValuesFromPoints(0.35,0.2)
#    for g in [0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.33,0.35]:
#        instance.setGc(g)
#        for pML1 in [99]:#[1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]:
#            instance.setProp(pML1)
#            instance.contourGif()
#        instance.saveSNR_List(g,0.2)
#        instance.savePoints(g,0.2)
#    instance.plotThesisHeterSpiralWaves()
#    instance.plotTypeIISpiralWaves()
#    instance.saveHeterSNR(0.22,0.2)
#    instance.saveHeterFiringRate(0.22,0.2)
#    instance.saveHeterPhaseOrder(0.22,0.2)
#    instance.saveSNRList(0,0.22,0.2)
#    for pML1 in [1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,99]:#range(0,101,5):
#        instance.setProp(pML1)
#        instance.saveSpiralWaves()

