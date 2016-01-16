from Constants import *
from utils import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


class process:
    def __init__(self, input_config):
        self.input_config = input_config

    def set_input_config(self,input_self):
        self.input_config = input_self

    def averAutoCorr(self, time_array):
        sumAutoCorr = None
        for time in time_array:
            matrix = self.input_config.inputSpiralWave(time)
            if sumAutoCorr == None:
                sumAutoCorr = autoCorr(matrix)
            else:
                sumAutoCorr = sumAutoCorr + autoCorr(matrix)

        averAC = sumAutoCorr / len(time_array)

        np.savetxt(os.path.join(self.input_config.pp_direct, u'%s_averAutoCorr.txt' % self.input_config.spec))
        # plt.

    def averSSF(self, time_array=time_array):
        sumSSF = None
        for time in time_array:
            matrix = self.input_config.inputSpiralWave(time)
            if sumSSF == None:
                sumSSF = np.square(np.fft.fft2(matrix))
            else:
                sumSSF = sumSSF + np.square(np.fft.fft2(matrix))

        rawSSF = sumSSF/len(time_array)
        averSSF = procSSF(rawSSF)

        np.savetxt(os.path.join(self.input_config.pp_direct, u'%s_averSSF.txt' % self.input_config.spec))




if __name__ == '__main__':
    xa = range(1, 4)
    ya = range(1, 4)
    z = [[1, 2, 3], [4, 5, 6], [1, 6, 7]]
    x, y = np.meshgrid(xa, ya)
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(projection='3d')
    Axes3D.plot(x,y,z)
    # ax.plot_surface(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    #plt.surf
    plt.show()
    plt.savefig('/Users/yes/1.png')
