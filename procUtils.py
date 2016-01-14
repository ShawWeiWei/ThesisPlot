from Constants import *
from utils import autoCorr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class process:
    def __init__(self, input_config):
        self.input_config = input_config

    def averAutoCorr(self, time_array=time_array):
        sumAutoCorr = None
        for time in time_array:
            matrix = self.input_config.inputSpiralWave(time)
            if sumAutoCorr == None:
                sumAutoCorr == autoCorr(matrix)
            else:
                sumAutoCorr = sumAutoCorr + autoCorr(matrix)

        averAC = sumAutoCorr / len(time_array)

        # plt.


if __name__ == '__main__':
    xa = range(1,4)
    ya = range(1,4)
    z = [[1,2,3],[4,5,6],[1,6,7]]
    x, y = np.meshgrid(xa, ya)
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(projection = '3d')
    ax.plot_surface(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.surf
    plt.show()
    plt.savefig('C:\\users\\shaw\\desktop\\1.png')
