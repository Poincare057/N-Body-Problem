# n-body code
import numpy as np
import matplotlib.pyplot as plt

# masses
n = 3
m = np.zeros(n)
for i in range(n):
    m[i] = float(input())
    
#constants
G = 6.67*10**-4

#simulation time and step size
T = 100000
h = 0.01

r = np.zeros((T, n, 3))

# Specifying structure of differential equations
def norm(l):
    return (l[0]**2 + l[1]**2 + l[2]**2)**0.5

def f(r):
    f = np.zeros((n,3))
    for i in range(n):
        for j in range(n):
            if j == i:
                pass
            else:
                f[i] += (G*m[i]*m[j]/norm(r[j]-r[i]))*(r[j]-r[i])
    return f

#Numerical Integration of the n-body system

#Initial Conditions
eps = 0.1
for i in range(n):
    for j in range(3):
        r[0][i][j] = float(input())
        r[1][i][j] = r[0][i][j] + eps*np.random.random()
        
for t in range(2, T):
    r[t] = 2*r[t-1] - r[t-2] + (h**2)*f(r[t-2])

def plot():
    rplot = np.zeros((T, 3))
    for i in range(n):
        for t in range(T):
            rplot[t] = r[t][i]
        plt.plot(rplot)
        rplot = np.zeros((T, 3))
    plt.show()

def config_plot(code):
    rplot = np.zeros((T))
    for t in range(T):
        rplot[t] = r[t][code[0]][code[1]]
    rplot2 = np.zeros((T))
    for t in range(T):
        rplot2[t] = r[t][code[2]][code[3]]
    plt.plot(rplot, rplot2)
    plt.show()



