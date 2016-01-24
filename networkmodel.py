import numpy as np
import matplotlib.pyplot as plt
from plotsetting import *

mpl.rcParams['lines.linewidth'] = 0.5

marker_size = 15
color_type = 'black'

N = 16
K = 2
R = 100.0
border = 10
angle = np.linspace(0, 2 * np.pi * (1.0 - 1.0 / float(N)), N)
x = R * np.cos(angle)
y = R * np.sin(angle)


def plotSquare():
    plt.clf()
    dim = 6
    for i in range(dim):
        for j in range(dim):
            plt.plot(i, j, 'k.', markersize=marker_size)
            if ((i - 1) >= 0):
                plt.plot([i - 1, i], [j, j], color='black')

            if ((i + 1) < dim):
                plt.plot([i + 1, i], [j, j], color='black')

            if ((j - 1) >= 0):
                plt.plot([i, i], [j - 1, j], color='black')

            if ((j + 1) < dim):
                plt.plot([i, i], [j + 1, j], color='black')
    plt.axis('equal')
    plt.axis('off')
    plt.title('(a)')
    plt.xlim([-2, dim + 1])
    plt.ylim([-2, dim + 1])
    plt.savefig('squareNetwork.tiff',dpi = 200)


def makeRegular():
    A = np.zeros((N, N), bool)
    for i in range(N):
        for j in range(1, K + 1):
            if (i + j) >= N:
                flag = i + j - N
                A[i, flag] = True
                A[flag, i] = True
            else:
                A[i, i + j] = True
                A[i + j, i] = True
    return A

def makeWSSmallWorld(p):
    A = makeRegular()
    for i in range(N):
        for j in range(i + 1, N):
            if A[i, j]:
               pp = np.random.rand()
               if pp < p:
                   A[i,j]=False
                   A[j,i]=False
                   b = np.random.randint(N)
                   while b == i:
                        b = np.random.randint(N)
                   A[i,b] = True
                   A[b,i] = True
    return A

def makeNWSmallWorld(p):
    A = makeRegular()
    for i in range(N):
        for j in range(i + 1, N):
            if not A[i, j]:
               pp = np.random.rand()
               if pp < p:
                   A[i,j]=True
                   A[j,i]=True
    return A

def plotRegular():
    plt.clf()

    plt.plot(x, y, 'k.', markersize=marker_size)

    A = makeRegular()
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])

    plt.axis('equal')
    plt.axis('off')
    plt.title('(b)')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    plt.savefig('Regular.tiff',dpi = 200)


def plotFullConnectedNetwork():
    plt.clf()
    plt.plot(x, y, 'k.', markersize=marker_size)

    for i in range(N):
        for j in range(N):
            plt.plot([x[i], x[j]], [y[i], y[j]])

    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    plt.title('(d)')
    plt.savefig('FullConnected.tiff',dpi = 200)

def plotStarCoupledNetwork():
    plt.clf()
    plt.plot(x, y, 'k.', markersize=marker_size)
    plt.plot(0,0,'k.',markersize = marker_size)

    for i in range(len(x)):
        plt.plot([0, x[i]], [0, y[i]])

    plt.axis('equal')
    plt.axis('off')
    plt.title('(c)')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    plt.savefig('StarConnected.tiff',dpi  = 200)


def plotWSSmallWorld(p):
    plt.clf()
    plt.plot(x, y, 'k.', markersize=marker_size)
    A = makeRegular()
    for i in range(N):
        for j in range(i + 1, N):
            if A[i, j]:
               pp = np.random.rand()
               if pp < p:
                   A[i,j]=False
                   A[j,i]=False
                   b = np.random.randint(N)
                   while b == i:
                        b = np.random.randint(N)
                   A[i,b] = True
                   A[b,i] = True


    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])


    plt.axis('equal')
    plt.axis('off')

    plt.xlim([-R - 3, R + 3])
    plt.ylim([-R - 3, R + 3])
    plt.savefig('WSSmallWorld%.5f.png'%p)

def plotNWSmallWorld(p):
    plt.clf()
    plt.plot(x, y, 'k.', markersize=marker_size)
    A = makeRegular()
    for i in range(N):
        for j in range(i + 1, N):
            if not A[i, j]:
               pp = np.random.rand()
               if pp < p:
                   A[i,j]=True
                   A[j,i]=True


    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])


    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - 3, R + 3])
    plt.ylim([-R - 3, R + 3])

    plt.savefig('NWSmallWorld%.5f.png'%p)

def plotGenerateSW():
    plt.clf()
    plt.subplot(131)
    A = makeRegular()
    plt.plot(x, y, 'k.', markersize=marker_size)
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    # plt.title('p = 0')
    plt.text(0,130,'(a)',ha = 'center', va = 'center')

    plt.subplot(132)
    A = makeWSSmallWorld(0.5)
    plt.plot(x, y, 'k.', markersize=marker_size)
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    # plt.title('p = 0.5')
    plt.text(0,130,'(b)',ha = 'center', va = 'center')

    plt.subplot(133)
    A = makeWSSmallWorld(1)
    plt.plot(x, y, 'k.', markersize=marker_size)
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    # plt.title('p = 1')
    plt.text(0,130,'(c)',ha = 'center', va = 'center')

    plt.savefig('Generate WS small world.tiff',dpi = 400)

def plotGenerateNW():
    plt.clf()
    plt.subplot(131)
    A = makeRegular()
    plt.plot(x, y, 'k.', markersize=marker_size)
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    # plt.title('p = 0')
    plt.text(0,130,'(a)',ha = 'center', va = 'center')

    plt.subplot(132)
    A = makeNWSmallWorld(0.5)
    plt.plot(x, y, 'k.', markersize=marker_size)
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    # plt.title('p = 0.5')
    plt.text(0,130,'(b)',ha = 'center', va = 'center')


    plt.subplot(133)
    A = makeNWSmallWorld(1)
    plt.plot(x, y, 'k.', markersize=marker_size)
    for i in range(N):
        for j in range(N):
            if A[i, j]:
                plt.plot([x[i], x[j]], [y[i], y[j]])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - border, R + border])
    plt.ylim([-R - border, R + border])
    # plt.title('p = 1')
    plt.text(0,130,'(c)',ha = 'center', va = 'center')

    plt.savefig('Generate NW small world.tiff',dpi = 400)

def plotGenerateSparser():
    dim = 6
    plt.clf()
    plt.subplot(131)
    for i in range(dim):
        for j in range(dim):
            plt.plot(i, j, 'k.', markersize=marker_size)
            if ((i - 1) >= 0):
                plt.plot([i - 1, i], [j, j], color='black')

            if ((i + 1) < dim):
                plt.plot([i + 1, i], [j, j], color='black')

            if ((j - 1) >= 0):
                plt.plot([i, i], [j - 1, j], color='black')

            if ((j + 1) < dim):
                plt.plot([i, i], [j + 1, j], color='black')
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-1, dim])
    plt.ylim([-1, dim])
    # plt.title('p = 0')
    plt.text(2.5,6,'p = 0',ha = 'center', va = 'center')
    plt.subplot(132)
    p = 0.1
    for i in range(dim):
        for j in range(dim):
            plt.plot(i, j, 'k.', markersize=marker_size)
            # if ((i - 1) >= 0 and np.random.rand() > p):
            #     plt.plot([i - 1, i], [j, j], color='black')

            if ((i + 1) < dim and np.random.rand() > p):
                plt.plot([i + 1, i], [j, j], color='black')

            # if ((j - 1) >= 0 and np.random.rand() > p):
            #     plt.plot([i, i], [j - 1, j], color='black')

            if ((j + 1) < dim and np.random.rand() > p):
                plt.plot([i, i], [j + 1, j], color='black')
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-1, dim])
    plt.ylim([-1, dim])
    # plt.title('p = 0.5')
    plt.text(2.5,6,'p = 0.1',ha = 'center', va = 'center')

    plt.subplot(133)
    p = 0.2
    for i in range(dim):
        for j in range(dim):
            plt.plot(i, j, 'k.', markersize=marker_size)
            # if ((i - 1) >= 0 and np.random.rand() > p):
            #     plt.plot([i - 1, i], [j, j], color='black')

            if ((i + 1) < dim and np.random.rand() > p):
                plt.plot([i + 1, i], [j, j], color='black')

            # if ((j - 1) >= 0 and np.random.rand() > p):
            #     plt.plot([i, i], [j - 1, j], color='black')

            if ((j + 1) < dim and np.random.rand() > p):
                plt.plot([i, i], [j + 1, j], color='black')
    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-1, dim])
    plt.ylim([-1, dim])
    # plt.title('p = 1')
    plt.text(2.5,6,'p = 0.2',ha = 'center', va = 'center')

    plt.savefig('Generate Sparser.tiff',dpi = 400)
if __name__ == '__main__':
    #plt.show()
    #plotSquare()
    #plotRegular()
    #plotFullConnectedNetwork()
    #plotStarCoupledNetwork()
    #plotFullConnectedNetwork()
    #plotSmallWorld(0.2)
    #plotGenerateSW()
    plotGenerateNW()
    #plotGenerateSparser()

