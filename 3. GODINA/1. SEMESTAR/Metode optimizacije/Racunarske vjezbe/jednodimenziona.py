import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.linalg as lin
from scipy import optimize

# Izvod polinoma
f=np.poly1d([-1, 5, 2, -24, 0])
prvi_izvod=f.deriv()
drugi_izvod=prvi_izvod.deriv()

def func(x):
    return -(x**4 - 5*x**3 - 2*x**2 + 24*x)

def njutn_rapson(x0, tol):
    iter=0
    x_novo=x0
    x_pre=math.inf
    while(abs(x_novo-x_pre)>tol):
        iter+=1
        x_pre=x_novo
        x_novo=x_pre-prvi_izvod(x_pre)/drugi_izvod(x_pre)
 
    xopt=x_novo
    fopt=f(xopt)
    return xopt, fopt, iter



def secica(x0, x1, tol):
    iter=0
    x_pre=x0
    x_ppre=math.inf
    x_novo=x1
    while(abs(x_novo-x_pre)>tol):
        iter+=1
        x_ppre=x_pre
        x_pre=x_novo
        x_novo=x_pre-prvi_izvod(x_pre)*(x_pre-x_ppre)/(prvi_izvod(x_pre)-prvi_izvod(x_ppre))
    xopt=x_novo
    fopt=func(xopt)
    return xopt, fopt, iter


def fibonaci_broj(n):
    x0=0
    x1=1
    if(n==1):
        return x1
    elif n==0:
        return x0
    else:
        for i in range(2, n):
            x_n=x0+x1
            x0=x1
            x1=x_n
    return x1


def fibonaci_metod(a, b, tol):
    n=0
    while((b-a)/tol)>fibonaci_broj(n):
        n+=1
    x1=a+(b-a)*(fibonaci_broj(n-2)/fibonaci_broj(n))
    x2=a+b-x1
    
    for i in range(2, n+1):  
        if (x1!=0 and x2!=0 ): 
            if(func(x1)<=func(x2)):
                b=x2
                x2=x1
                x1=a+b-x2
            else:
                a=x1
                x1=x2
                x2=a+b-x1
    
    if func(x1)<=func(x2):
        xopt=x1
    else:
        xopt=x2
    
    fopt=func(xopt)
    return xopt, fopt, n


def zlatni_presek(a, b, tol):
    iter=0
    c=(3-math.sqrt(5))/2
    x1=a+c*(b-a)
    x2=a+b-x1
    while (abs(b-a))>tol :
        iter+=1
        if(func(x1)<=func(x2)):
            b=x2
        else:
            a=x1
        x1=a+c*(b-a)
        x2=a+b-x1
    if(func(x1)<func(x2)):
        xopt=x1
    else:
        xopt=x2
    fopt=func(xopt)

    return xopt, fopt, iter

def parabola(x1, x3, tol):
    X = np.array([x1, (x1 + x3)/2, x3])
    F = np.array([func(x1), func((x1 + x3)/2), func(x3)])
    
    Y = np.vstack([np.ones(3), X, X**2]).T
    abc = lin.solve(Y, F)
    
    x = -abc[1]/2/abc[2]
    fx = func(x)
    n = 0
    
    while np.abs(np.dot([1, x, x**2], abc) - fx) > tol:
        if x > X[1]:
            if fx < F[1] and fx < F[2]:
                X = np.array([X[1], x, X[2]])
                F = np.array([F[1], fx, F[2]])
            elif fx > F[1] and fx < F[2]:
                X = np.array([X[0], X[1], x])
                F = np.array([F[0], F[1], fx])
            else:
                print('Error: minimum is not a local minimum')
        elif x < X[1]:
            if fx < F[0] and fx < F[1]:
                X = np.array([X[0], x, X[2]])
                F = np.array([F[0], fx, F[2]])
            elif fx > F[1] and fx < F[0]:
                X = np.array([x, X[1], X[2]])
                F = np.array([fx, F[1], F[2]])
            else:
                print('Error: minimum is not a local minimum')
        else:
            print('Error: minimum is not within bounds')
        
        Y = np.vstack([np.ones(3), X, X**2]).T
        abc = lin.solve(Y, F)
        
        x = -abc[1]/2/abc[2]
        fx = func(x)
        n += 1
        
    return x, fx, n


tol=0.01
x0=-1
x1=-2
a = 0
b = 2

[xopt, fopt, iteracije] = njutn_rapson(x0, tol)
# [xopt, fopt, iteracije] = secica(x0, x1, tol)
# [xopt, fopt, iteracije] = fibonaci_metod(a, b, tol)
# [xopt, fopt, iteracije] = zlatni_presek(a, b, tol)
#[xopt, fopt, iteracije] = parabola(a, b, tol)
print(xopt, fopt)
# plot
x=np.linspace(-3, 5, 1000)
f=np.linspace(0,0,1000)
for i in range(0, len(x), 1):
    f[i]=func(x[i])
p = plt.plot(x, f)
p = plt.plot(xopt, fopt, 'or', markersize = 15)
plt.show()
