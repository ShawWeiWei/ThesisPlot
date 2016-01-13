# -*- coding: utf-8 -*-
import numpy as np


#归一化处理
def fft_wrapper(t,x):
    Fs=1/(t[1]-t[0]); # 采样点数和采样频率，Fs=1/0.1
    N=np.size(x);
    if N!=np.size(t):
        return

    z=np.mean(x);
    y=x-z;
    ret=[]
    p=np.abs(np.fft.fft(y,N));  #功率谱
    power=p*p;
    f=np.linspace(0,(N-1)*Fs/N,N)
    ret.append(f)
    ret.append(power)
    ret=np.array(ret)
    ret=ret.transpose()
    return ret


    
def fft_unormalized(t,x):
    RawPower=fft_wrapper(t,x)   
    s=np.size(RawPower[:,0])
    half=RawPower[0:s/2+1,:]
 #   half[:,1]=half[:,1]/np.sum(half[:,1])
    return half
            
def fft_normalized(t,x):
    RawPower=fft_wrapper(t,x)   
    s=np.size(RawPower[:,0])
    half=RawPower[0:s/2+1,:]
    half[:,1]=half[:,1]/np.sum(half[:,1])
    return half
    
def findMaxFre(t,x):
    if np.size(t)!=np.size(x):
        return
    index=0
    maxV=x[0]
    s=np.size(x)
    for i in range(s/2):
        if x[i]>maxV:
            index=i
            maxV=x[i]
    return index
def findSecondMaxFre(t,x,i):
    if np.size(t)!=np.size(x):
        return
    index=0
    maxV=x[0]
    s=np.size(x)
    for j in range(s/2):
        if x[j]>maxV and j!=i:
            index=j
            maxV=x[j]            
    return index
                