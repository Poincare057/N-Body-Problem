##CODE TO NUMERICALLY INTEGRATE THE N-BODY PROBLEM

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Number of bodies
n = 3

#UI Stuff
coord = ["x", "y", "z"]

# masses
m = np.zeros(n)
for i in range(n):
    m[i] = float(input("Enter mass of " + str(i) + "-th body: "))
print()

#constants
G = 6.67*10**-4

#simulation time and step size
T = 100000
h = 0.01

# Specifying structure of differential equations
r = np.zeros((T, n, 3))     #Positions of all the n bodies in 3D space from time [0, T*h]

def norm(l):                                    #Magnitude of a vector (L2 norm)
    return (l[0]**2 + l[1]**2 + l[2]**2)**0.5                       

def f(r):                   #In the differential equation d^2 r_i/dt^2 = f_i(r), where r = (r_1, ..., r_n), and r_i = (x_i, y_i, z_i), f(r) returns all the f_i
    f = np.zeros((n,3))
    for i in range(n):
        for j in range(n):
            if j == i:
                pass
            else:
                f[i] += (G*m[i]*m[j]/norm(r[j]-r[i]))*(r[j]-r[i])
    return f

#Numerical Integration of the n-body system

eps = 0.1   #Initial condition for derivative

for i in range(n):
    for j in range(3):
        r[0][i][j] = float(input(coord[j] + " coordinate of " + str(i) + "-th body: "))
        r[1][i][j] = r[0][i][j] + eps*np.random.random()
    print()
        
for t in range(2, T):
    r[t] = 2*r[t-1] - r[t-2] + (h**2)*f(r[t-2])

#plots motion of each coordinate of each body through time
def plot():
    rplot = np.zeros((T, 3))
    for i in range(n):
        for t in range(T):
            rplot[t] = r[t][i]
        plt.plot(rplot)
        rplot = np.zeros((T, 3))
    plt.show()

#3D sections of the configuration space
def config_plot3D(code):
    rplot = np.zeros((T))
    for t in range(T):
        rplot[t] = r[t][code[0]][code[1]]
    rplot2 = np.zeros((T))
    for t in range(T):
        rplot2[t] = r[t][code[2]][code[3]]
    rplot3 = np.zeros((T))
    for t in range(T):
        rplot3[t] = r[t][code[4]][code[5]]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot(rplot, rplot2, rplot3)
    plt.show()

#2D sections of configuration space
def config_plot2D(code):
    rplot = np.zeros((T))
    for t in range(T):
        rplot[t] = r[t][code[0]][code[1]]
    rplot2 = np.zeros((T))
    for t in range(T):
        rplot2[t] = r[t][code[2]][code[3]]
    plt.plot(rplot, rplot2)
    plt.show()

#plots 3D trajectories of all the n bodies
def plot_all():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    for i in range(n):
        rplot = np.zeros((T))
        for t in range(T):
            rplot[t] = r[t][i][0]
        rplot2 = np.zeros((T))
        for t in range(T):
            rplot2[t] = r[t][i][1]
        rplot3 = np.zeros((T))
        for t in range(T):
            rplot3[t] = r[t][i][2]
        ax.plot(rplot, rplot2, rplot3)
    plt.show()
        
    


