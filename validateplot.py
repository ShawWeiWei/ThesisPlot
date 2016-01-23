import matplotlib.pyplot as plt
import os
import numpy as np
def plotDegreeDistribution():
    aP = [0,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
    direct = u'F:\\validate'
    aDegree = []
    for p in aP:
        data = np.loadtxt(os.path.join(direct,'pML1=1%%_Sparser_%.5f_Degree.dat'%p))
        aDegree.append(np.average(data))

    plt.clf()
    plt.plot(aP,aDegree)
    plt.show()

if __name__ == '__main__':
    plotDegreeDistribution()