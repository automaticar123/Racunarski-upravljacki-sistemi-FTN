import math

def zlatni_presek(a, b, tol):
    c=(3-math.sqrt(5))/2
    x1 = a + c*(b-a)
    x2 = a + b - x1
    n=1
    while ((abs(b-a))>tol): 
        n+=1
        if func(x1)<=func(x2):
            b=x2
        else:
            a=x1

        x1 = a + c*(b-a)
        x2 = a + b - x1

    if func(x1)<func(x2):
        xopt=x1
        fopt=func(x1)
    else:
        xopt=x2
        fopt=func(x2)

    return xopt, fopt, n

def func(x):
    f=-1*(x**4-5*x**3-2*x**2+24*x)
    return f

[xopt, fopt, n]=zlatni_presek(0, 3, 0.0001)
print(xopt, fopt, n)