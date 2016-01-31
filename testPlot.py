#from plotsetting import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
def proc(a):
    return np.mean(a)

def plotSyn(tau1,tau2):
    potential=np.loadtxt('F:\\NeuroComput\\tau1=%.5f_tau2=%.5f_potential.dat'%(tau1,tau2))
    current0= np.loadtxt('F:\\NeuroComput\\tau1=%.5f_tau2=%.5f_current_%d.dat'%(tau1,tau2,0))
    current1= np.loadtxt('F:\\NeuroComput\\tau1=%.5f_tau2=%.5f_current_%d.dat'%(tau1,tau2,1))
    current2= np.loadtxt('F:\\NeuroComput\\tau1=%.5f_tau2=%.5f_current_%d.dat'%(tau1,tau2,2))

    fig=plt.figure()
    t_max_idx=list(current0[:,1]).index(max(current0[:,1]))
    rise_time = current0[t_max_idx,0]-current0[0,0]
    t_zero_time = current0[-1,0]
    for i,val in enumerate(current0[:,1]):
        if i>t_max_idx and current0[i,1]<0.00001:
            t_zero_time = current0[i,0]

    decay_time = t_zero_time - current0[t_max_idx,0]

    ax1=fig.add_subplot(411)
    ax1.set_title('''tau1 = %.4f_tau2=%.4f
                rise_time=%.4f_decay_time=%.4f'''%(tau1,tau2,rise_time,decay_time))
    ax2=fig.add_subplot(412)
    ax3=fig.add_subplot(413)
    ax4=fig.add_subplot(414)

    line_width=2
    font_size=15
    ax1.plot(potential[:,0],potential[:,1],'k-',linewidth=line_width)
    ax1.set_ylabel(r'$V$',fontsize=font_size)
    ax1.set_yticks([-60,-25,-10,5,40])
    ax1.set_xlim([0,300])
    ax1.set_xticklabels([])
    #ax1.get_xaxis().set_visible(False)


    ax2.plot(current0[:,0],current0[:,1],'y-',linewidth=line_width)
    ax2.set_xlim([0,300])
    ax2.set_ylim([0,1])
    ax2.set_yticks([0,0.5,1])
    #ax2.get_xaxis().set_visible(False)
    ax2.set_ylabel(r'spike 1',fontsize=font_size)
    ax2.set_xticklabels([])


    ax3.plot(current1[:,0],current1[:,1],'r-',linewidth=line_width)
    ax3.set_xlim([0,300])
    ax3.set_ylim([0,1])
    ax3.set_yticks([0,0.5,1])
    ax3.set_ylabel(r'spike 2',fontsize=font_size)
    ax3.set_xticklabels([])
    #ax3.get_xaxis().set_visible(False)

    ax4.plot(current2[:,0],current2[:,1],'b-',linewidth=line_width)
    ax4.set_ylim([0,1])
    ax4.set_xlim([0,300])
    ax4.set_yticks([0,0.5,1])
    ax4.set_ylabel(r'spike 3' ,fontsize=font_size)
    ax4.set_xlabel('time',fontsize=font_size)

    if not os.path.exists('F:\\NeuroComputPlot\\plot'):
         os.makedirs('F:\\NeuroComputPlot\\plot')
    plt.savefig('F:\\NeuroComputPlot\\plot\\tau1=%.5f_tau2=%.5f_potential.png'%(tau1,tau2))

    plt.close()
if __name__ == '__main__':
    for i in range(1,11):
        for j in range(1,11):
            if i != j:
                plotSyn(2*i,2*j)
    # line = plt.plot([1,3,4],':',markersize = 100)
    # plt.xlabel('$\mathrm{g_s} =$ $\mathrm{\mu S / cm^2}$')
    # plt.ylabel('TESTTEST')
    #
    # plt.subplots_adjust(left = 0.14,bottom = 0.14,right = 0.9,top = 0.9)
    # plt.show()
    # plt.savefig('c:\\users\\shaw\\desktop\\1.png')

