from Constants import *
from utils import autoCorr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


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

        np.savetxt(os.path.join(self.input_config.pp_direct, u'%s_averAutoCorr.txt' % self.input_config.spec))
        # plt.

    def ssf(self):
        matrix=load(filenameIn);
        F=fft2(matrix);
        abs_H=abs(F);
        H=H+abs_H.*abs_H;

%        mesh(x,y,container);
%        xlim([1,128]);
%        ylim([1,128]);
%        saveas(gcf,sprintf('%s\\%s_AC_t=%.5f.png',pathOut,coupleAndNoise,t(idx3)));
%        a=normalize1(matrix);
%        s=sum(sum(a));
%        if s>max
%            max=s;
%            max_idx=idx3;
%        end
    end
    HH=H./size(t,2);


    S=fftshift(HH);
    SS=[S(1:n/2,1:n);zeros(1,n);S(n/2+1:n,1:n)];
    SSS=[SS(1:n+1,1:n/2),zeros(n+1,1),SS(1:n+1,n/2+1:n)];%%%%%%%%%%%%%%中间加入一行一列零


if __name__ == '__main__':
    xa = range(1, 4)
    ya = range(1, 4)
    z = [[1, 2, 3], [4, 5, 6], [1, 6, 7]]
    x, y = np.meshgrid(xa, ya)
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.surf
    plt.show()
    plt.savefig('C:\\users\\shaw\\desktop\\1.png')
