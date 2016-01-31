# -*- coding: utf-8 -*-
#每个环所包含的离散点
import numpy as np
import matplotlib.pyplot as plt
import os
#from mayavi import mlab
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

b=[]
dim=range(0,50)
width = 2
for i in dim:
    for j in range(i+1):
        b.append(np.sqrt(i*i+j*j))
b=sorted(b)
                        
#time_array=np.linspace(2020,4980,149)
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
    return (2.0*ACofRadius[kb]-ACofRadius[ka]-ACofRadius[kc])/(kc-ka)#,ka,kb,kc
    
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
    return 2.0*FFT2ofRadius[kb]/(FFT2ofRadius[ka]+FFT2ofRadius[kc])#,ka,kb,kc
    
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
    width = 1.5
    for r in range(50):
        listFFT2=[]
        for i in dim:
            for j in dim:
                rr = np.sqrt(i*i+j*j)
                if  rr >= (r-width) and rr <=(r+width):#int(rr+0.5) == r:
                    listFFT2.append(data[i][j])
        FFT2ofRadius.append([r,np.average(listFFT2)])
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


     
def FFT_SNR(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs):
    filename_Part=filenamePart(synaptic,network,Connor,HH,ML1,ML2,Inh,Inh_NoCoupling,noise,*tupleargs)
    filename=u'F:\\postprocess\\FFT\\%s_FFT.dat'%\
        (filename_Part)
    data=np.loadtxt(filename)
    ACOfRadius=makeACList(data)
    return firstPeak(ACOfRadius)

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
    

    
def plot3d(gc):
    #aGc_cE=np.linspace(0.2,0.3,21)
    aNoise=[0.00001,0.00002,0.00005,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]
    for noise in aNoise:
        data=np.loadtxt(u'F:\\postprocess\\AC\\Sigmoidal\\Square\\Connor0HH0ML1_16384ML2_0Inh_(0,0)\\gc_exc=%.5f_gc_inh=%.5f_noise=%.5f_AC_square_average_sum.dat'%(gc,gc,noise))
        fig.clear()
        X=np.linspace(0,128)#(min(data[:,1]),max(data[:,0]),(max(data[:,0])-min(data[:,1]))/0.1+2)
        Y=np.linspace(0,128)#(min(data[:,1]),max(data[:,1]),(max(data[:,1])-min(data[:,1]))/0.1+2)
        x,y=np.meshgrid(X,Y)
        #mlab.surf(x,y,data,warp_scale="auto")
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
    for pML1 in aML1:
        plt.figure()
        fileIn=os.path.join(pathIn,u'%s_FFT2_Average.dat'%(specification))
        data=np.loadtxt(fileIn)
        listFFT2=makeFFT2List(data)
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
        aIndicator_Rec.append(indicator)
        fileOut=os.path.join(pathOut,u'%s_FFT2_Average_List.png'%(specification))
        plt.savefig(fileOut)
    plt.figure()
    plt.plot(aML1,aIndicator)
    fileOut=u'F:\\Verify\\Visual\\gc=%.5f_FFT2_Average_SNR.png'%(gc)
    plt.savefig(fileOut)

if __name__=='__main__':



      FFT2_SNR(0.22)

      
