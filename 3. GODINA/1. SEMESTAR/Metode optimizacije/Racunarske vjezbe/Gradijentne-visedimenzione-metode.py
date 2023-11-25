import numpy as np
import matplotlib.pyplot as plt

#Metod najbrzeg pada(obicni gradijentni algoritam)

def steepest_descent(gradf, x0, gamma, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1)

    for k in range(N):
        g = gradf(x)
        x = x - gamma * g
        if np.linalg.norm(g) < epsilon:
            break
    
    return x

def steepest_descent_with_momentum_v(gradf, x0, gamma, epsilon, omega, N):
    x = [np.array(x0).reshape(len(x0), 1)]
    v = np.zeros(shape = x[-1].shape)

    for k in range(N):
        g = gradf(x[-1])
        v = omega * v + gamma * g
        x.append(x[-1] - v)

        if np.linalg.norm(g) < epsilon:
            break

    return x

def adam_v(gradf, x0, gamma, omega1, omega2, epsilon1, epsilon, N):
    x = [np.array(x0).reshape(len(x0), 1)]
    v = [np.ones(shape = x[-1].shape)]
    m = [np.ones(shape = x[-1].shape)]

    for k in range(N):
        g = np.asarray(gradf(x[-1]))
        m.append(omega1 * m[-1] + (1 - omega1) * g)
        v.append(omega2 * v[-1] + (1 - omega2) * np.multiply(g, g))

        hat_v = np.abs(v[-1]/(1 - omega2))
        hat_m = m[-1]/(1 - omega1)
        x.append(x[-1] - gamma * np.ones(shape = g.shape)/np.sqrt(hat_v + epsilon1) * hat_m)

        if np.linalg.norm(g) < epsilon:
            break
    
    return x, v, m

def quadratic(x, M, reshape = True):
    if reshape:
        x = np.reshape(x, newshape = (len(x), 1))

    val = 1/2 * np.transpose(x) @ M @ x

    return val[0, 0]

def quadratic_grad(x, M, reshape = True):
    if reshape:
        x = np.array(x).reshape(len(x), 1)

    return M @ x

def steepest_descent_v(gradf, x0, gamma, epsilon, N):
    x = [np.array(x0).reshape(len(x0), 1)]

    for k in range(N):
        g = gradf(x[-1])
        x.append(x[-1] - gamma*g)
        if np.linalg.norm(g) < epsilon:
            break
    return x

print(steepest_descent(lambda x: quadratic_grad(x, np.eye(2)), [1, 2], 1, 1e-4, 100))

print(steepest_descent_with_momentum_v(lambda x: quadratic_grad(x, np.eye(2)), x0 = [3, 0.1], gamma = 0.15 * 0.1, epsilon = 1e-4, omega = 0.15 * 0.9, N = 100))

print(adam_v(lambda x: quadratic(x, np.eye(2)), x0 = [3, 0.1], gamma = 0.091, omega1 = 0.9, omega2 = 0.99, epsilon1 = 1e-6, epsilon = 1e-6, N = 100))