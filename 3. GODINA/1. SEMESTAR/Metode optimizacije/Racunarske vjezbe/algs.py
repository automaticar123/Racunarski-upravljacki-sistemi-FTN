import sympy as sp
import numpy as np

def func(x: np.ndarray) -> float:
    return x[0]**2 + x[1]**2

def grad_func(x: np.ndarray) -> np.ndarray:
    return np.array([2*x[0], 2*x[1]])

def steepest_descent(x0: np.ndarray, tollerance: float, gamma: float) -> tuple:
    x = x0

    while True:
        g = grad_func(x)
        x = x - gamma * g

        if np.linalg.norm(g) < tollerance:
            break

    return x, func(x)

def steepest_descent_with_momentum(x0: np.ndarray, tollerance: float, gamma: float, omega: float) -> tuple:
    x = x0
    v = np.zeros(x0.shape)

    while True:
        g = grad_func(x)
        v = omega * v + gamma * g
        x = x - v

        if np.linalg.norm(g) < tollerance:
            break

    return x, func(x)

def adam(x0: np.ndarray, tollerance: float, gamma: float, omega1: float, omega2: float) -> tuple:
    x = x0
    v = np.zeros(x0.shape)
    m = np.zeros(x0.shape)

    for i in range(100):
        g = grad_func(x)
        m = omega1 * m + (1 - omega1) * g
        v = omega2 * v + (1 - omega2) * np.multiply(g, g)

        m_hat = m / (1 - omega1)
        v_hat = np.abs(v) / (1 - omega2)

        x = x - gamma * m_hat / np.sqrt(v_hat + 1e-6)

        if np.linalg.norm(g) < tollerance:
            break

    return x, func(x)


print(steepest_descent(np.array([2, 2]), 1e-5, 0.1))
print(steepest_descent_with_momentum(np.array([2, 2]), 1e-5, 0.05, 0.5))
print(adam(np.array([2, 2]), 1e-6, 0.15, 0.9, 0.99))

