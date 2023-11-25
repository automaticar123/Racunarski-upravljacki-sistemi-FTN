import numpy as np
import matplotlib.pyplot as plt
import math 
from mpl_toolkits.mplot3d import Axes3D

"""
x1 = np.arange(-5, 5, 0.01)
x2 = np.arange(-5, 5, 0.01)

X1, X2 = np.meshgrid(x1, x2)

Y = np.sin(X1) + np.cos(X2)
fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.plot_surface(X1, X2, Y)
plt.show()
"""

def Ackley(ulaz, a, b):
    first = 0
    second = 0
    for i in range(0, len(ulaz)):
        first = first + ulaz[i]**2
        second = second + np.cos(ulaz[i] * 2 * np.pi)
    
    first = -a * np.exp(-b * np.sqrt((1/len(ulaz)) * first))
    second = np.exp((1/len(ulaz)) * second)

    return first + second + a + np.exp(1)

def Griewalk(ulaz):
    sum = 0
    mul = 1

    for i in range(1, len(ulaz)):
        sum = sum + (1/4000) * ulaz[i-1]**2
        mul = mul * np.cos(ulaz[i-1] / np.sqrt(i))
    
    return sum - mul + 1

x1 = np.arange(-5, 5, 0.01)
x2 = np.arange(-5, 5, 0.01)

X1, X2 = np.meshgrid(x1, x2)

Y = Ackley([X1, X2], 20, 0.2)
Y1 = Griewalk([X1, X2])

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.plot_surface(X1, X2, Y1)

plt.show()

