import numpy as np
import sympy as sp

def func(x: np.ndarray):
    return float(2 * x[0]**2 - 1.05 * x[0]**4 + 1/6 * x[0]**6 + x[0] * x[1] + x[1]**2)

def gfunc(x: np.ndarray):
    return np.array([[float(x[0])**5 - 4.2*float(x[0])**3 + 4*float(x[0]) + float(x[1])], [float(x[0]) + 2*float(x[1])]])

def mgrad(start: np.ndarray, gamma: float, omega: float, tollerance: float, N: int):

    x = start
    g = np.inf
    v = 0

    g = gfunc(x)

    for i in range(N):

        v = omega * v + gamma * g
        x = x - v

        g = gfunc(x)

        if np.linalg.norm(g) < tollerance:
            break

    return x, func(x), i

def f(x: float):
    return np.cos(2*x) - np.sin(1 + x)

def golden_ratio(a: float, b: float, tollerance: float):
    
    c = 1/float(sp.S.GoldenRatio)**2

    x1 = a + c*(b - a)
    x2 = a + b - x1

    while np.abs(b - a) > tollerance:

        if(f(x1) >= f(x2)):
            a = x1
            x1 = x2
            x2 = a + b - x2
            print(a, b)
        
        else:
            b = x2
            x2 = x1
            x1 = a + b - x1
            print(a, b)

    if(f(x1) >= f(x2)):
        return x2, f(x2)
    else:
        return x1, f(x1)

#print(mgrad(np.array([[-1], [1]]), 0.3, 0.1, 1e-4, 100))
print(golden_ratio(0.5, 2, 1e-1))
