# -*- coding: utf-8 -*-
#每个环所包含的离散点
import numpy as np
import matplotlib.pyplot as plt
import os
from mayavi import mlab
def savitzky_golay(y, window_size, order, deriv=0, rate=1):

    import numpy as np
    from math import factorial

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')
    
#for above functions 
a=[[]]*100
row_dim=range(0,100)
column_dim=range(0,100)
for i in row_dim:
    for j in column_dim:
        radius=int(np.sqrt(i*i+j*j)+0.5)
        if radius<100:
            a[radius]=a[radius]+[[i,j]]
        else:
            pass

b=[[]]*50
row_dim=range(0,50)
column_dim=range(0,50)
for i in row_dim:
    for j in column_dim:
        radius=int(np.sqrt(i*i+j*j)+0.5)
        if radius<50:
            b[radius]=b[radius]+[[i,j]]
        else:
            pass
                        
time_array=np.linspace(2020,4980,149)
composition=u''
coupleAndNoise=u''
#################################

def nextMax(listin,start):
    list_size=len(listin)
    if start>=list_size-1:
        return 0
    for i in range(start,list_size-1):
        if listin[i]>listin[i+1]:
            return i
        else:
            pass
            
    return list_size-1
    
def nextMin(listin,start):
    list_size=len(listin)
    if start>=list_size-1:
        return 0
    for i in range(start,list_size-1):
        if listin[i]<listin[i+1]:
            return i
        else:
            pass
    return list_size-1

def firstPeakAC(ACofRadius):
    list_size=len(ACofRadius)
    ka=nextMin(ACofRadius,0)
    if ka==list_size-1 or ka==0:
        return 0
    #print ka,ACofRadius[ka]
    kb=nextMax(ACofRadius,ka)
    if kb==list_size-1:
        return 0
    #print kb,ACofRadius[kb]
    kc=nextMin(ACofRadius,kb)    
    
    #print kc,ACofRadius[kc]
    return (2.0*ACofRadius[kb]-ACofRadius[ka]-ACofRadius[kc])/(kc-ka),ka,kb,kc
    
def MaximumLeftAndRightMinimum(listAC):
    list_size=len(listAC)
    ka=nextMin(listAC,0)
    if ka==list_size-1:
        return 0
        
    maximum=ka+1
    for i in range(ka+1,list_size):
        if listAC[i]>listAC[maximum]:
            maximum=i
    
    leftminimum=ka
    for i in range(ka,maximum):
        if listAC[i]<listAC[leftminimum]:
            leftminimum=i
            
    if maximum==list_size-1:
        return leftminimum,maximum,maximum
    
    rightminimum=nextMin(listAC,maximum)
            
    return leftminimum,maximum,rightminimum

    
def firstPeakAC_Rec(ACofRadius):
    list_size=len(ACofRadius)
    ka=nextMin(ACofRadius,0)
    if ka==list_size-1 or ka==0:
        return 0
    #print ka,ACofRadius[ka]
    kb=nextMax(ACofRadius,ka)
    if kb==list_size-1:
        return 0
    #print kb,ACofRadius[kb]
    kc=nextMin(ACofRadius,kb)    

    #print kc,ACofRadius[kc]
    return ((ACofRadius[kb]-ACofRadius[ka])/(kb-ka)+(ACofRadius[kb]-ACofRadius[kc])/(kc-kb))/2.0,ka,kb,kc
    #return (2.0*ACofRadius[kb]-ACofRadius[ka]-ACofRadius[kc])/(kc-ka),ka,kb,kc

def firstPeakFFT2(FFT2ofRadius):
    list_size=len(FFT2ofRadius)
    ka=nextMin(FFT2ofRadius,0)
    if ka==list_size-1 or ka==0:
        return 0
    #print ka,ACofRadius[ka]
    kb=nextMax(FFT2ofRadius,ka)
    if kb==list_size-1:
        return 0
    #print kb,ACofRadius[kb]
    kc=nextMin(FFT2ofRadius,kb)    
    
    #print kc,ACofRadius[kc]
    return 2.0*FFT2ofRadius[kb]/(FFT2ofRadius[ka]+FFT2ofRadius[kc]),ka,kb,kc
    
def firstPeakFFT2_Rec(FFT2ofRadius):
    list_size=len(FFT2ofRadius)
    ka=nextMin(FFT2ofRadius,0)
    if ka==list_size-1 or ka==0:
        return 0
    #print ka,ACofRadius[ka]
    kb=nextMax(FFT2ofRadius,ka)
    if kb==list_size-1:
        return 0
    #print kb,ACofRadius[kb]
    kc=nextMin(FFT2ofRadius,kb)    
    
    #print kc,ACofRadius[kc]
    return 2.0*FFT2ofRadius[kb]/(FFT2ofRadius[ka]+FFT2ofRadius[kc]),ka,kb,kc
    
def makeACList(data):
    ACofRadius=[]
    for i in a:
        listAC=[]
        for j in i:
            listAC.append(data[j[0]][j[1]])
        ACofRadius.append(np.mean(listAC))
        del listAC
    return ACofRadius
    
def makeFFT2List(data):
    FFT2ofRadius=[]
    for i in b:
        listFFT2=[]
#        print i
        for j in i:
            listFFT2.append(data[j[0]][j[1]])
#        print listFFT2
        FFT2ofRadius.append(np.average(listFFT2))
#        print np.average(listFFT2)
        del listFFT2
    return FFT2ofRadius 
    
def makeIntegralList(data):
    IntegralList=[]
    for i in a:
        listAC=[]
        for j in i:
            listAC.append(data[j[0]][j[1]])
        Integral=np.average(listAC)*i
    IntegralList.append(Integral)
        
def filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs):
    if np.size(tupleargs)==2:
        coupleAndNoise=u'gc_exc=%.5f_gc_inh=%.5f_noise=%.5f'%(tupleargs[0],tupleargs[1],noise)
        composition=u'Connor%dHH%dML1_%dML2_%dInh_(%d,%d)'%(Connor,HH,ML1,ML2,Inh,Inh_NoCoupling)
    else: 
        coupleAndNoise=u'gc=%.5f_noise=%.5f'%(tupleargs[0],noise)
        composition=u'Connor%dHH%dML1_%dML2_%d'%(Connor,HH,ML1,ML2)
    filename_Part=u'%s\\%s\\%s\\%s'%(synaptic,network,composition,coupleAndNoise)
    return filename_Part

def FFT_ACOfRadius(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs):   
    filename_Part=filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs)
    filename=u'F:\\postprocess\\FFT\\%s_FFT.dat'%\
        (filename_Part)
    data=np.loadtxt(filename)
    ACOfRadius=makeACList(data)
    return ACOfRadius
     
def FFT_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs):
    filename_Part=filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs)
    filename=u'F:\\postprocess\\FFT\\%s_FFT.dat'%\
        (filename_Part)
    data=np.loadtxt(filename)
    ACOfRadius=makeACList(data)
    return firstPeak(ACOfRadius)
    
def diffNoiseFFT_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,aNoise,*tupleargs):
    list_SNR=[]
    for noise in aNoise:
        list_SNR.append(FFT_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs))
    return list_SNR
       
def diffTimeAC_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs):
    filename_Part=filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs)
    snr=[]
    for t in time_array:
        filename=u'F:\\postprocess\\AC\\%s_t=%.5fAC.dat'%\
                (filename_Part,t)     
        data=np.loadtxt(filename)
        ACList=makeACList(data)
        snr.append(firstPeak(ACList))
    return snr




def plotDiffTimeAC_SNR():
    aGc_cE=np.linspace(0.2,0.3,21)
    aNoise=[0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]
    listPeak=[]
    for t in time_array:
        data=np.loadtxt(u'F:\\postprocess\\AC\\Sigmoidal\\Square\\Connor0HH0ML1_16384ML2_0Inh_(0,0)\\gc_exc=0.26000_gc_inh=0.26000_noise=0.00200_t=%.5fAC.dat'%(t))
        listAC=[]
        listAC=makeACList(data)
        listPeak.append(firstPeak(listAC))
    plt.plot(time_array,listPeak)
    plt.xlabel(u't')
    plt.ylabel(u'SNR')
    plt.title(u'different time in certain parameters')
    plt.show()
#for gc_ce in aGc_cE:
#    snr=[]
#    fig=plt.figure()
#    for noise in aNoise:
#        snr.append(np.mean(diffTimeFirstPeak(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,gc_ce,gc_ce)))
#    #    print str(noise)+' is done'
#    plt.plot(aNoise,snr)
#    plt.xscale('log')
#    plt.title(u'gc=%.5f'%(gc_ce))
#    plt.xlabel(u'noise')
#    plt.ylabel(u'SNR')
#    plt.show()
#    
#    if synaptic==synaptic_Sigmoidal:
#        filename=u'C:\\users\\shaw\\desktop\\Sigmoidal1\\Connor%dHH%dML1_%dML2_%dInh_(%d,%d)\\gc_exc=%.5f_gc_inh=%.5f_SNR.png'%\
#        (Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,gc_ce,gc_ce)
#    else:
#        filename=u'c:\\users\\shaw\\desktop\\Electrical\\Connor%dHH%dML1_%dML2_%d\\gc=%.5f_SNR.png'%\
#        (Connor,HH,ML1,ML2,gc_ce)
#    path=filename.split('\\gc')[0]
#    if os.path.exists(path):
#        pass
#    else:
#        os.makedirs(path)
#        
#    plt.savefig(filename)
    
    
def sumOfMatrix(m):
    return sum(sum(m))
    
def plot3d(gc):
    #aGc_cE=np.linspace(0.2,0.3,21)
    aNoise=[0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]
    for noise in aNoise:
        data=np.loadtxt(u'F:\\postprocess\\AC\\Sigmoidal\\Square\\Connor0HH0ML1_16384ML2_0Inh_(0,0)\\gc_exc=%.5f_gc_inh=%.5f_noise=%.5f_AC_square_average_sum.dat'%(gc,gc,noise))
        fig.clear()
        X=np.linspace(0,128)#(min(data[:,1]),max(data[:,0]),(max(data[:,0])-min(data[:,1]))/0.1+2)
        Y=np.linspace(0,128)#(min(data[:,1]),max(data[:,1]),(max(data[:,1])-min(data[:,1]))/0.1+2)
        x,y=np.meshgrid(X,Y)
        mlab.surf(x,y,data,warp_scale="auto")
        plt.xlabel(u'{\Symbol a}')
        plt.ylabel(u'{\Symbol b}')
        plt.xlim([1,128]);
        plt.ylim([1,128]);
        #plt.title(u'')
        #plt.show()
        outfilename=u'F:\\Graduation Thesis\\spiral wave animation\\Sigmoidal\\Square\\Connor0HH0ML1_16384ML2_0Inh_(0,0)\\gc_exc=%.5f_gc_inh=%.5f_noise=%.5f_AC_square_average_sum.tiff'\
        %(gc,gc,noise)
        plt.savefig(outfilename)
    
def plotAC_Square_Average_Sum(gc):
    aNoise=[0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]
    listQI=[]
    for noise in aNoise:
        data=np.loadtxt(u'F:\\postprocess\\AC\\Sigmoidal\\Square\\Connor0HH0ML1_16384ML2_0Inh_(0,0)\\gc_exc=%.5f_gc_inh=%.5f_noise=%.5f_AC_square_average_sum.dat'%(gc,gc,noise))
        QI=sumOfMatrix(data)
        print QI
        print np.size(QI)
        listQI.append(QI)
    fig.clear()
    plt.plot(aNoise,listQI)
    plt.xlabel(u'd')
    plt.ylabel(u'QI')
    #plt.title(u'')
    #plt.show()
    outfilename=u'F:\\Graduation Thesis\\spiral wave animation\\Sigmoidal\\Square\\Connor0HH0ML1_16384ML2_0Inh_(0,0)\\gc_exc=%.5f_gc_inh=%.5f_QI_AC.tiff'\
    %(gc,gc)
    plt.savefig(outfilename)  

def AC_SNR(gc):    
    aIndicator=[]
    aIndicator_Rec=[]
    Vsyn=30
    threshold=-25
    I_Span=0.2
    for pML1 in aML1:
        plt.figure()
        pathIn=u'F:\\Verify\\PP\\ML1_%d'%(pML1)
        pathOut=u'F:\\Verify\\Visual\\ML1_%d'%(pML1)
        specification=u'gc_exc=%.5f_Vsyn=%.5f_threshold=%.5f_RandI(%.5f,%.5f)_AC_Average1.dat'%(gc,Vsyn,threshold,I_Span,I_Span);
        fileIn=os.path.join(pathIn,specification)
        data=np.loadtxt(fileIn)
        listAC=makeACList(data)
        plt.subplot(211)
        plt.plot(listAC)
        result=firstPeakAC(listAC)
        plt.scatter(result[1],listAC[result[1]])
        plt.scatter(result[2],listAC[result[2]])
        plt.scatter(result[3],listAC[result[3]])
        plt.title('%.5f'%(result[0]))
        aIndicator.append(result[0])
#          listAC=savitzky_golay(np.array(listAC),61,3)
        plt.subplot(212)
        plt.plot(listAC)
        result=firstPeakAC_Rec(listAC)
        plt.scatter(result[1],listAC[result[1]])
        plt.scatter(result[2],listAC[result[2]])
        plt.scatter(result[3],listAC[result[3]])
        plt.title('%.5f'%(result[0]))
        aIndicator_Rec.append(result[0])
        fileOut=os.path.join(pathOut,u'%s_ListAC.tiff'%(specification))
        plt.savefig(fileOut)
    plt.figure()
    plt.subplot(211)
    plt.plot(aIndicator)    
    plt.subplot(212)
    plt.plot(aIndicator_Rec)
    fileOut=u'F:\\Verify\\Visual\\gc=%.5f_AC_Average_SNR.tiff'%(gc)
    plt.savefig() 
    
def FFT2_SNR(gc):    
    aIndicator=[]
    aIndicator_Rec=[]
    Vsyn=30
    threshold=-25
    I_Span=0.2
    for pML1 in aML1:
        plt.figure()
        pathIn=u'F:\\Verify\\PP\\ML1_%d'%(pML1)
        pathOut=u'F:\\Verify\\Visual\\ML1_%d'%(pML1)
        specification=u'gc_exc=%.5f_Vsyn=%.5f_threshold=%.5f_RandI(%.5f,%.5f)'%(gc,Vsyn,threshold,I_Span,I_Span);
        fileIn=os.path.join(pathIn,u'%s_FFT2_Average.dat'%(specification))
        data=np.loadtxt(fileIn)
#        print data
        listFFT2=makeFFT2List(data)
#        print listFFT2
#        plt.subplot(211)
        plt.plot(listFFT2)
        plt.yscale('log')
        result=firstPeakFFT2(listFFT2)
        if type(result)==tuple:
            plt.scatter(result[1],listFFT2[result[1]])
            plt.scatter(result[2],listFFT2[result[2]])
            plt.scatter(result[3],listFFT2[result[3]])
            indicator=result[0]
        else:
            indicator=result
        print indicator
        plt.title('%.5f'%(indicator))
        aIndicator.append(indicator)
#          listAC=savitzky_golay(np.array(listAC),61,3)
#        plt.subplot(212)
#        plt.plot(listFFT2)
#        result=firstPeakFFT2_Rec(listFFT2)
#        plt.scatter(result[1],listFFT2[result[1]])
#        plt.scatter(result[2],listFFT2[result[2]])
#        plt.scatter(result[3],listFFT2[result[3]])
#        plt.title('%.5f'%(result[0]))
        aIndicator_Rec.append(indicator)
        fileOut=os.path.join(pathOut,u'%s_FFT2_Average_List.png'%(specification))
        plt.savefig(fileOut)
    plt.figure()
#    plt.subplot(211)
    plt.plot(aML1,aIndicator)    
#    plt.subplot(212)
#    plt.plot(aIndicator_Rec)
    fileOut=u'F:\\Verify\\Visual\\gc=%.5f_FFT2_Average_SNR.png'%(gc)
    plt.savefig(fileOut)    
if __name__=='__main__':
      Connor=0
      HH=0
      ML2=0#int(16384.0*percentageOfMl2/100.0+0.5)#16384#-ML1-819
      Inh=0#int(16384.0*percentageOfInh/100.0+0.5)
      ML1=16384#16384-ML2-Inh#int(16384*0.05*i+0.5)#14746#16384#14746#15565#16384#6400#13107-3277
      Inh_NoCoupling=0
      tau1=2.0
      tau1=2.0
      tau2=1.0
      gc_cE=0.26#0.2
      gc_cI=0.26#0.05
      gc_e=1.0
      noise=0.005
      Vs=30
      threshold=-25
      rewiring=0.5
      sparse=0.5#i
      #    project1=u'OnlyForTest'
        #    project2=u'视皮层网络'
      #    project3=u'视皮层网络beta'
      synaptic_Electrical=u'Electrical'
      synaptic_Spike=u'Spike'
      synaptic_Sigmoidal=u'Sigmoidal'
      network_Square=u'Square'
      network_SmallWorld=u'SmallWorld_%.2f'%(rewiring)
      network_Sparser=u'Sparser_%.2f'%(sparse)
    
      synaptic=synaptic_Sigmoidal
      network=network_Square
      
      aGc_ce=[0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3]
      aNoise=[0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]
      
      
      gc_cE=0.2 
      gc_cI=0.05
      noise=0.005
      
      aML1=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
      Vsyn=30
      threshold=-25
      gc=0.22
      I_Span=0.2
      FFT2_SNR(0.22)
#          aAC=[]
#          for t in time_array:
              #
              
#              fileIn=os.path.join(pathIn,u'%s_t=%.5f.dat'%(specification,t))
              
#              data=np.loadtxt(fileIn)
#              listAC=makeACList(data)
#              result=firstPeakAC(listAC)
#              aAC.append(result[0])
              
#          aIndicator.append(np.mean(aAC))
          #plt.title(u'indicator=%.5f'%(result[0]))
          #plt.scatter(result[1],listAC[result[1]])
          #plt.scatter(result[2],listAC[result[2]])
          #plt.scatter(result[3],listAC[result[3]])
 #         plt.plot(aAC)
 #         fileOut=os.path.join(pathOut,u'%s.png'%(specification))
 #         plt.savefig(fileOut)
        
#      plt.figure()
#      plt.plot(aML1,aIndicator)
#      plt.savefig(u'F:\\Verify\\Visual\\gc=%.5f_AC_AverageBefore1.png'%(gc));
      
#      fig=plt.figure()
#      plot3d(0.26)
#      for gc in aGc_ce:
#          plotAC_Square_Average_Sum(gc)
#      for pML2 in percentageofML2:
#          print
#          for pInh in percentageofInh:
#              ML2=int(16384.0*pML2/100.0+0.5)
#              Inh=int(16384.0*pInh/100.0+0.5)
#              ML1=16384-ML2-Inh
#              print FFT_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,gc_cE,gc_cI),
            
       
        
#      for gc_cE in aGc_ce:
#          fig=plt.figure()
#          plt.plot(aNoise,diffNoiseFFT_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,aNoise,gc_cE,gc_cE))
#          filename_Part=filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,aNoise[0],gc_cE,gc_cE)
#          ofilename=u'F:\\Graduation Thesis\\spiral wave animation\\'+filename_Part.split('_noise')[0]+'_SNR.png'
#          plt.title('gc_exc=%.5f gc_inh=%.5f'%(gc_cE,gc_cE))
#          plt.xlabel('noise')
#          plt.xscale('log')
#          plt.ylabel('SNR')
#          plt.yscale('log')
#          plt.savefig(ofilename)
#          for noise in aNoise:
#            list_FFT_AC=FFT_ACOfRadius(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,gc_cE,gc_cE)
#            SNR=firstPeak(list_FFT_AC)
#            fig=plt.figure()
#            plt.plot(list_FFT_AC)
#            plt.yscale('log')
            #plt.show()
#            plt.title('gc_exc=%.5f gc_inh=%.5f noise=%.5f'%(gc_cE,gc_cE,noise))
#            plt.xlabel('radius')
#            plt.ylabel('average of ring')
#            filename_Part=filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,gc_cE,gc_cE)
#            ofilename=u'F:\\Graduation Thesis\\spiral wave animation\\%s_average_of_ring.png'%(filename_Part)
#            plt.savefig(ofilename)
      