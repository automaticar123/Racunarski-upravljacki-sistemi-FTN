import math

def secica(x1, x0, tol):
    x_pre=x0
    x_ppre=math.inf
    x_novo=x1
    iter=0
    while(abs(x_novo-x_pre)>tol):
        iter+=1
        x_ppre = x_pre
        x_pre = x_novo
        x_novo = x_pre- dfunc(x_pre)*(x_pre-x_ppre)/(dfunc(x_pre)-dfunc(x_ppre))
    xopt=x_novo
    fopt=func(xopt)
    return xopt, fopt, iter

def func(x):
    f=x**4-5*x**3-2*x**2+24*x
    return f
def dfunc(x):
    f=4*x**3-15*x**2-4*x+24
    return f

[xopt, fopt, iter]=secica(0, 3, 0.0001)
print(xopt, fopt, iter)
