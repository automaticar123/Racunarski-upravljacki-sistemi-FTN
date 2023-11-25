import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
"""
def func(x: np.ndarray) -> float:
    return (0.01*(x[0] - 1)**2 + 0.02*(x[1] - 1)**2)*((x[0] + 1)**2 + 2*(x[1] + 1)**2 + 0.5)*((x[0] + 2)**2 + 2*(x[1] - 2)**2 + 0.7)

def grad(x: np.ndarray) -> np.ndarray:
    return np.array([(0.02*x[0] - 0.02)*((x[0] + 1)**2 + 2*(x[1] + 1)**2 + 0.5)*((x[0] + 2)**2 + 2*(x[1] - 2)**2 + 0.7) + (2*x[0] + 2)*(0.01*(x[0] - 1)**2 + 0.02*(x[1] - 1)**2)*((x[0] + 2)**2 + 2*(x[1] - 2)**2 + 0.7) + (2*x[0] + 4)*(0.01*(x[0] - 1)**2 + 0.02*(x[1] - 1)**2)*((x[0] + 1)**2 + 2*(x[1] + 1)**2 + 0.5), 
    (0.04*x[1] - 0.04)*((x[0] + 1)**2 + 2*(x[1] + 1)**2 + 0.5)*((x[0] + 2)**2 + 2*(x[1] - 2)**2 + 0.7) + (4*x[1] - 8)*(0.01*(x[0] - 1)**2 + 0.02*(x[1] - 1)**2)*((x[0] + 1)**2 + 2*(x[1] + 1)**2 + 0.5) + (4*x[1] + 4)*(0.01*(x[0] - 1)**2 + 0.02*(x[1] - 1)**2)*((x[0] + 2)**2 + 2*(x[1] - 2)**2 + 0.7)])
"""
def func(x: np.ndarray) -> float:
    print(type(x[0]**2 + x[1]**2 + np.sin(x[0]) + np.cos(x[1])))
    return x[0]**2 + x[1]**2 + np.sin(x[0]) + np.cos(x[1])

def grad(x: np.ndarray) -> np.ndarray:
    return np.array([2*x[0] + np.cos(x[0]), 2*x[1] - np.sin(x[1])])


def optimum_grad(x0: np.ndarray, tollerance: float, gamma: float):
    x = x0
    while True:
       g = grad(x)
       x = x - gamma * g
       k = np.linalg.norm(g)
       if np.linalg.norm(g) < tollerance:
        break

    return x, func(x)

def optimum_momentum(x0: np.ndarray, tollerance: float, gamma: float, omega: float):
    v = np.zeros(x0.shape)
    x = x0

    while True:
        g = grad(x)
        v = omega*v + gamma*g
        x = x - v
        if np.linalg.norm(g) < tollerance:
            break
    
    return x, func(x)

def adam(x0: np.ndarray, tollerance: float, epsilon: float, omega1: float, omega2: float, gamma: float):
    m = np.ones(x0.shape)
    v = np.ones(x0.shape)
    x = x0

    for i in range(1000):
        g = grad(x)
        m = omega1 * m + (1 - omega1) * g
        v = omega2 * m + (1 - omega2) * np.multiply(g, g)

        m_hat = m / (1 - omega1)
        v_hat = np.abs(v / (1 - omega2))

        x = x - (gamma / np.sqrt(v_hat + epsilon)) * m_hat
    
    return x, func(x)


x = sp.symbols('x[0]')
y = sp.symbols('x[1]')
f = 0.01 * ((x-1)**2 + 2*(y-1)**2) * ((x+1)**2 + 2*(y+1)**2 + 0.5) * ((x+2)**2 + 2*(y-2)**2 + 0.7)
print(sp.diff(f, x))
print(sp.diff(f, y))

print(optimum_grad(np.array([-2, 2]), 0.000001, 0.15))
print(optimum_momentum(np.array([-2, 2]), 0.000001, 0.15, 0.1))
print(adam(np.array([-2, -2]), 0.0001, 0.0001, 0.9, 0.999, 0.1))
















