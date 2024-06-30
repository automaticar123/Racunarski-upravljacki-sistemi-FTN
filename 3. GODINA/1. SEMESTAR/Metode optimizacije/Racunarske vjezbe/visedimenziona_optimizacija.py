import numpy as np
import sympy as sp
#import matplotlib.pyplot as plt

def f(x):
    return 0.01*((x[0]-4)**2+2*(x[1]-4)**2)*((x[0]+5)**2+2*(x[1]-5)**2+7)

#IZVOD - iz print prepisi u "gradf"
x1=sp.symbols('x1')
x2=sp.symbols('x2')
f=0.01*((x1-4)**2+2*(x2-4)**2)*((x1+5)**2+2*(x2-5)**2+7)
dx1=f.diff(x1)
dx2=f.diff(x2)
print('Izvod po x:', dx1, '\nIzvod po y:', dx2)

def gradf(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[(0.02*x[0] - 0.08)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (2*x[0] + 10)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)],
                [(0.04*x[1] - 0.16)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (4*x[1] - 20)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)]])


def steepest_descent(gradf, x0, gama, epsilon=0.01, N=100):
    x = np.array(x0).reshape(len(x0), 1)
    for i in range(N):
        grad = gradf(x)
        x = x-gama*grad
        if np.linalg.norm(grad) < epsilon:
            break
    return x


def steepest_descent_momentum(gradf, x0, gama=0.1, epsilon=0.01, omega=0.5, N=100):
    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(x.shape)
    for i in range(N):
        grad = gradf(x)
        v = omega * v + gama * grad
        x -= v
        if np.linalg.norm(grad) < epsilon:
            break
    return x


def steepest_descent_nesterov(gradf, x0, gama=0.1, epsilon=0.01, omega=0.5, N=100):
    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(x.shape)
    for i in range(N):
        xp = x - omega * v
        grad = gradf(xp)
        v = omega * v + gama * grad
        x = x-v
        if np.linalg.norm(grad) < epsilon:
            break
    return x


def adagrad(gradf, x0, gama, epsilon, e1, N):
    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(x.shape)
    G = np.zeros(x.shape)

    for i in range(N):
        grad = gradf(x)
        G = G + np.multiply(grad,grad)
        v = gama / np.sqrt(G+e1) * grad
        x = x-v
        if np.linalg.norm(grad) < epsilon:
            break
    return x

def adam(gradf, x0, gama, epsilon, omega1, omega2, e1, N):
    x = np.array(x0).reshape(len(x0), 1)
    m = np.zeros(x.shape)
    v = np.zeros(x.shape)

    for i in range(N):
        grad = gradf(x)
        m = m*omega1+(1-omega1)*grad
        v = v*omega2+(1-omega2)*np.multiply(grad,grad)

        m_hat = m / (1-omega1)
        v_hat = v / (1-omega2)

        x = x - gama * m_hat / np.sqrt(v_hat+e1) 
        if np.linalg.norm(grad) < epsilon:
            break
    return x

xopt = steepest_descent(gradf, [-1, 1], 0.1)
print(xopt, f(xopt))

#xopt = steepest_descent_momentum(gradf, [-1, 1], 0.1)
#print(xopt)
#xopt = steepest_descent_nesterov(gradf, [-1, 1], 0.1)
#print(xopt)
#xopt = adagrad(gradf, [-1, 1], 0.2, 0.01, 1e-8, 100)
#print(xopt)
#xopt = rmsprop(gradf, [-1, 1], 0.05, 0.01, 1e-8, 0.9, 100)
#print(xopt)
#xopt = adam(gradf, [-1, 1], 0.1, 0.01, 0.1, 0.9, 1e-8, 100)
#print(xopt)


#x1v = np.arange(-6, 6, 0.01)
#x2v = np.arange(-6, 6, 0.01)
#x1, x2 = np.meshgrid(x1v, x2v)
#z = f([x1, x2])

#fig = plt.figure()
#ax = fig.gca(projection="3d")
#ax.plot_surface(x1, x2, z)
#plt.show()