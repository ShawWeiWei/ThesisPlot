# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
N=10#input('Please input N:')
m0=3
m=3 #初始化网络数据
adjacent_matrix=np.zeros((N,N)) #初始化邻接矩阵
for i in range(m0):
    for j in range(m0):
        if j!=i:      #去除每个点自身形成的环
            adjacent_matrix[i,j]=1 #建立初始邻接矩阵，3点同均同其他的点相连
angle=2*np.pi/m0*ml.frange(0,m0-1)
x=100*np.cos(angle)
y=100*np.sin(angle)
x1=120*np.cos(angle)
y1=120*np.sin(angle)
plt.figure(1)
plt.subplot(151)
plt.hold(True)
for i in range(m0):
    for j in range(m0):
        if adjacent_matrix[i,j]==1:
            plt.plot([x[i],x[j]],[y[i],y[j]],color='black',linewidth=1)
plt.plot(x,y,'r.',markersize=20)
for i in range(m0):
    plt.text(x1[i],y1[i],'%d'%(i+1),horizontalalignment='center',verticalalignment='center')
plt.axis('equal')
plt.axis('off')
#plt.title('N=%d'%m0)
plt.show()
#adjacent_matrix=sparse(adjacent_matrix); #邻接矩阵稀疏化
node_degree=np.zeros(N+1)                #初始化点的度
node_degree[1:m0+1]=np.sum(adjacent_matrix[0:m0,0:m0],axis=0) #对度维数进行扩展
for iter in range(m0+1,N+1):
    iter                                #加点
    total_degree=2*m*(iter-4)+6#计算网络中此点的度之和
    cum_degree=np.cumsum(node_degree)#求出网络中点的度矩阵
    choose= np.zeros(m)#初始化选择矩阵
    # 选出第一个和新点相连接的顶点
    r1= np.random.random_sample()*total_degree#算出与旧点相连的概率
    for i in range(iter-1):
        if (r1>=cum_degree[i])and( r1<cum_degree[i+1]):#选取度大的点
            choose[0] = i
            break

    #选出第二个和新点相连接的顶点
    r2= np.random.random_sample()*total_degree;
    for i in range(iter-1):
        if (r2>=cum_degree[i])and(r2<cum_degree[i+1]):
            choose[1]= i
            break

    while choose[1]==choose[0]:#第一个点和第二个点相同的话，重新择优
        r2= np.random.random_sample()*total_degree
        for i in range(iter-1):
            if (r2>=cum_degree[i])and(r2<cum_degree[i+1]):
                choose[1] = i
                break
    # 选出第三个和新点相连接的顶点
    r3= np.random.random_sample()*total_degree
    for i in range(iter-1):
        if  (r3>=cum_degree[i])and(r3<cum_degree[i+1]):
            choose[2] = i
            break

    while (choose[2]==choose[0])or(choose[2]==choose[1]):
        r3= np.random.random_sample()*total_degree
        for i in range(iter-1):
            if (r3>=cum_degree[i])and(r3<cum_degree[i+1]):
                choose[2]=i
                break

    #新点加入网络后, 对邻接矩阵进行更新
    for k in range(m):
        adjacent_matrix[iter-1,choose[k]] = 1;
        adjacent_matrix[choose[k],iter-1] = 1;

    node_degree[1:iter+1]=np.sum(adjacent_matrix[0:iter,0:iter],axis=0);
    if iter==4 or iter==5 or iter==6:
        angle=2*np.pi/iter*ml.frange(0,iter-1)
        x=100*np.cos(angle)
        y=100*np.sin(angle)
        x1=120*np.cos(angle)
        y1=120*np.sin(angle)
 #       plt.figure()
        plt.subplot(150+iter-2)
        plt.hold(True)
        for i in range(iter):
            for j in range(iter):
                if adjacent_matrix[i,j]==1:
                    if (i!=iter-1)and(j!=iter-1):
                        plt.plot([x[i],x[j]],[y[i],y[j]],color='black',linewidth=1)
                    else:
                        plt.plot([x[i],x[j]],[y[i],y[j]],color='blue',linewidth=2)
        plt.plot(x[0:iter-1],y[0:iter-1],'r.',markersize=20)
        plt.plot(x[iter-1],y[iter-1],'y.',markersize=20)
        for i in range(iter):
            plt.text(x1[i],y1[i],'%d'%(i+1),horizontalalignment='center',verticalalignment='center')
        plt.axis('equal')
        plt.axis('off')
       # plt.title('N=%d'%iter)
        plt.show()

matrix = adjacent_matrix;

angle=2*np.pi/N*ml.frange(0,N-1)
x=100*np.cos(angle)
y=100*np.sin(angle)
x1=120*np.cos(angle)
y1=120*np.sin(angle)
#plt.figure()
plt.subplot(155)
plt.hold(True)
for i in range(N):
    for j in range(N):
        if matrix[i,j]==1:
            if (i!=N-1)and(j!=N-1):
                plt.plot([x[i],x[j]],[y[i],y[j]],color='black',linewidth=1)
            else:
                plt.plot([x[i],x[j]],[y[i],y[j]],color='blue',linewidth=2)
plt.plot(x[0:N-1],y[0:N-1],'r.',markersize=20)
plt.plot(x[N-1],y[N-1],'y.',markersize=20)
for i in range(N):
    plt.text(x1[i],y1[i],'%d'%(i+1),horizontalalignment='center',verticalalignment='center')
plt.axis('equal')
plt.axis('off')
#plt.title('N=%d'%N)
plt.show()