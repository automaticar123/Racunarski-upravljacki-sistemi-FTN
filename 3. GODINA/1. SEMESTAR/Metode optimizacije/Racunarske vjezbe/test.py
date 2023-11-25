import numpy as np
import sympy as sp

def func(x: float) -> float:
    return x**2 + np.sin(x)

def dfunc(x: float) -> float:
    return 2*x + np.cos(x)

def ddfunc(x: float) -> float:
    return 2 - np.sin(x)

def fibonacci_generator(n: int) -> int:
    
    fib_1 = 1
    fib_2 = 1

    if n == 1 or n == 2: 
        return 1

    for i in range(2, n):
        fib_n = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib_n

    return fib_n
        
# Njutn - Rapson
def newton_rapson(start: float, tollerance: float):
    
    xk = float(np.inf)
    xk1 = start
    n = 0
    
    while(np.abs(xk1 - xk) > tollerance):
        xk = xk1
        xk1 = xk - dfunc(xk)/ddfunc(xk)
        
        n += 1

    return xk1, func(xk1), n

# Metoda sjecice
def cut(start1: float, start2: float, tollerance: float):
    
    xk = float(np.inf)    #x[k]
    xk_1 = start2         #x[k-1]
    xk1 = start1          #x[k+1]

    n = 0

    while(np.abs(xk1 - xk) > tollerance):
        xk = xk1
        xk1 = xk - dfunc(xk) * (xk - xk_1) / (dfunc(xk) - dfunc(xk_1))
        xk_1 = xk

        n += 1

    return xk1, func(xk1), n

# Fibonaci metod, minimum
def fibonacci(a: float, b: float, tollerance: float):
    
    iter = 1
    
    while (int((b - a)/tollerance) > fibonacci_generator(iter)):
        iter += 1

    x1 = a + (b - a) * fibonacci_generator(iter - 2) / fibonacci_generator(iter)
    x2 = a + b - x1

    for _ in range(2, iter+1):

        if(func(x1) >= func(x2)):
            a = x1
            x1 = x2
            x2 = a + b - x1

        else:
            b = x2
            x2 = x1
            x1 = a + b - x2

    if(func(x1) >= func(x2)):
        return x2, func(x2), iter
    
    else:
        return x1, func(x1), iter

# Metod zlatnog presjeka, minimum
def golden_ratio(a: float, b:float, tollerance: float):
    
    c = float(3/2 - np.sqrt(5)/2)

    x1 = a + c * (b - a)
    x2 = a + b - x1

    iter = 0

    while ((b - a) > tollerance):
        iter += 1
        if(func(x1) >= func(x2)):
            a = x1
            x1 = x2
            x2 = a + b - x1
        else:
            b = x2
            x2 = x1
            x1 = a + b - x2

    if(func(x1) >= func(x2)):
        return x2, func(x2), iter
    else:
        return x1, func(x1), iter

# Metod parabole
def poly(dot_one: float, dot_two: float, dot_three: float, tollerance: float):
    x1 = dot_one
    x2 = dot_two
    x3 = dot_three

    f = 0
    g = np.inf

    n = 0

    while (np.abs(g - f) > tollerance):
        A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]]) 
        b = np.array([[func(x1)], [func(x2)], [func(x3)]])

        params = np.linalg.inv(A) @ b

        x_opt = float((-1) * params[1] / (2 * params[0]))

        if(x_opt > x2):
            x1 = x2
            x2 = x_opt
        else:
            x3 = x2
            x2 = x_opt

        f = func(x_opt)
        g = float(np.array([x_opt**2, x_opt, 1]) @ params) 

        n += 1

    return x_opt, f, n 

def gfunc(x: np.ndarray) -> float:
    return x[0]**2 + x[1]**2

def ggrad(x: np.ndarray):
    k = x[1]
    return np.array([[float(2 * x[1])], [float(2 * x[0])]])

# Gradijentni metod
def grad(start: np.ndarray, gamma: float, tollerance: float):
    
    x = start
    g = np.inf

    n = 0

    while np.linalg.norm(g) > tollerance:
        g = ggrad(x)
        x = x - gamma * g
        #k = np.linalg.norm(g)
        n += 1

    return x, gfunc(x), n

# Gradijentni metod sa momentom
def mgrad(start: np.ndarray, omega: float, gamma: float, tollerance: float):
    
    x = start
    g = np.inf
    v = 0

    n = 0

    while np.linalg.norm(g) > tollerance:
        
        g = ggrad(x)
        v = omega * v + gamma * g
        x = x - v

        n += 1

    return x, gfunc(x), n

#Nestorov
def nestorov(start: np.ndarray, omega: float, gamma: float, tollerance: float):

    dots_vector = []
    #dots_vector.append(np.array([[0], [0]]))

    x = start
    g = np.inf
    v = 0

    n = 0

    while np.linalg.norm(g) > tollerance:
        
        dots_vector.append(x)

        xp = dots_vector[-1] - omega * v
        g = ggrad(xp)
        v = omega * v + gamma * g
        x = x - v

        n += 1

    return x, gfunc(x), n

# Adaptivni gradijentni
def adagrad(start: np.ndarray, gamma: float, tollerance: float):
    
    x = start
    g = np.inf

    G0 = 0
    G1 = 0

    n = 0

    while np.linalg.norm(g) > tollerance:

        g = ggrad(x)

        G0 += float(g[0])**2
        G1 += float(g[1])**2

        x[0] = x[0] - gamma * g[0] / np.sqrt(G0 + 1e-6)
        x[1] = x[1] - gamma * g[1] / np.sqrt(G1 + 1e-6)

        n += 1
        
    return x, gfunc(x), n

# ADAM
def adam(start: np.ndarray, omega1: float, omega2: float, gamma: float, tollerance: float):
    
    x = start
    v = np.zeros(start.shape)
    m = np.zeros(start.shape)

    for i in range(10000):
        g = ggrad(x)
        m = omega1 * m + (1 - omega1) * g
        v = omega2 * v + (1 - omega2) * np.multiply(g, g)

        m_hat = m / (1 - omega1)    
        v_hat = np.abs(v / (1 - omega2))

        x = x - gamma * m_hat / np.sqrt(v_hat + 1e-5)

        if np.linalg.norm(g) < tollerance:
            break

    return x, gfunc(x), i


print(newton_rapson(-2, 1e-6))
print(cut(-4, -2, 1e-6))
print(fibonacci(-2, 2, 1e-3))
print(golden_ratio(-2, 2, 1e-3))
print(poly(-1, -0.5, 0, 1e-6))
print(grad(np.array([[-2], [-2]]), 0.8, 1e-5))
print(mgrad(np.array([[-2], [-2]]), 0.01, 0.8, 1e-5))
print(nestorov(np.array([[-2], [-2]]), 0.01, 0.8, 1e-5))
print(adagrad(np.array([[-2], [-2]]), 0.01, 1e-5))
print(adam(np.array([[-1], [-1]]), 0.9, 0.99, 0.8, 1e-6))








    

