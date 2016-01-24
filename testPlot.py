from plotsetting import *
import numpy as np

def proc(a):
    return np.mean(a)
if __name__ == '__main__':
    b=proc

    print b([1,2])