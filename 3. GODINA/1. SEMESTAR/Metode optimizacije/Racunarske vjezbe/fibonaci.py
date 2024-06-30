def fibonaci_broj(k):
    broj0=0
    broj1=1
    if(k==0):
        return broj0
    elif(k==1):
        return broj1
    else:
        for i in range(2, k+1):
            broj_k=broj0+broj1
            broj0=broj1
            broj1=broj_k
    return broj1

def fibonaci(a, b, tol):
    n=1
    while((b-a)/tol)>fibonaci_broj(n):
        n+=1
    
    x1=a + fibonaci_broj(n-2)/fibonaci_broj(n)*(b-a)
    x2=a + b - x1

    for i in range(2, n+1):
        if func(x1)<=func(x2):
            b=x2
            x2=x1
            x1=a+b-x2
        else:
            a=x1
            x1=x2
            x2=a+b-x1

    if(func(x1)<func(x2)):
        xopt=x1
        fopt=func(x1)
    else:
        xopt=x2
        fopt=func(x2)

    return xopt, fopt, n

def func(x):
    f=-1*(x**4-5*x**3-2*x**2+24*x)
    return f

[xopt, fopt, n]=fibonaci(0, 3, 0.0001)
print(xopt, fopt, n)
