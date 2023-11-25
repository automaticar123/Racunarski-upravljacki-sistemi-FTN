import numpy as np
import math

def func(x: float) -> float:
    return 8*x**4 - 3*x**2 + 9 

def poly(xx1: float, xx2: float, xx3: float, tollerance: float):
    x1 = xx1
    x2 = xx2
    x3 = xx3

    g = np.inf
    f = 0

    n = 0

    while np.abs(g - f) > tollerance:
        n += 1
        b = np.array([[func(x1)], [func(x2)], [func(x3)]])
        A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])

        params = np.dot(np.linalg.inv(A), b)
        opt_x = float(-params[1] / (2 * params[0]))

        if(x2 > opt_x):
            x3 = x2
            x2 = opt_x
        else:
            x1 = x2
            x2 = opt_x

        f = func(opt_x)    
        g = np.dot(np.array([opt_x**2, opt_x, 1]), params)

    return x2, func(x2), n

opt, fopt, n = poly(-2, -1, -0.3, 1e-5)

print(opt, fopt, n)