from plotsetting import *
import numpy as np
import matplotlib.pyplot as plt

def proc(a):
    return np.mean(a)
if __name__ == '__main__':
    plt.plot([1,3,4])
    plt.xlabel('$\mathrm{g_s} =$ $\mathrm{\mu S / cm^2}$')
    plt.ylabel('TESTTEST')

    plt.subplots_adjust(left = 0.14,bottom = 0.14,right = 0.9,top = 0.9)
    plt.show()
    # plt.savefig('c:\\users\\shaw\\desktop\\1.png')