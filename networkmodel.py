import numpy as np
import matplotlib.pyplot as plt
from plotsetting import *

mpl.rcParams['lines.linewidth'] = 1

marker_size = 20
color_type = 'black'

N = 16
K = 2
R = 100.0

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

            if ((j + 1) < 0):
                plt.plot([i, i], [j + 1, j], color='black')
    plt.axis('equal')
    plt.axis('off')

    plt.xlim([-2, dim + 1])
    plt.ylim([-2, dim + 1])
    plt.savefig('square1.png')


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

    plt.xlim([-R - 3, R + 3])
    plt.ylim([-R - 3, R + 3])
    plt.savefig('Regular.png')


def plotFullConnectedNetwork():
    plt.clf()
    plt.plot(x, y, 'k.', markersize=marker_size)

    for i in range(N):
        for j in range(N):
            plt.plot([x[i], x[j]], [y[i], y[j]])

    plt.axis('equal')
    plt.axis('off')
    plt.xlim([-R - 3, R + 3])
    plt.ylim([-R - 3, R + 3])
    plt.savefig('FullConnected.png')


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



if __name__ == '__main__':
    # plotSquare()
    # plotRegular()
    #plotFullConnectedNetwork()
#    plotSmallWorld(0.2)
