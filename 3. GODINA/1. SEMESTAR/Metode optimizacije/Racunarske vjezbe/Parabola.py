import numpy as np

def parabola(x1, x3, tol):
    X = np.array([x1, (x1 + x3)/2, x3]).transpose()
    pom = np.array([1, 1, 1]).transpose()
    Y = np.array([pom, X, X*X]).transpose()
    F = np.linspace(0, 0, len(X))

    for i in range(len(X)):
        F[i] = func(X[i])

    abc = np.linalg.solve(Y, F)
    x = -abc[1]/(2*abc[2])
    fX = func(x)

    n = 0
    while np.abs(np.dot([1, x, x**2], abc) - fX) > tol:
        if(x > X[1]) and (x < X[2]):
            if(fX < F[1]) and (fX < F[2]):
                X = np.array([X[1], x, X[2]])
                F = np.array([F[1], fX, F[2]])
            elif (fX > F[1]) and (fX < F[2]):
                X = np.array([X[0], X[1], x])
                F = np.array([F[0], F[1], fX])
        elif (x > X[0]) and (x < X[2]):
            if(fX < F[0]) and (fX < F[1]):
                X = np.array([X[0], x, X[2]])
                F = np.array([F[0], fX, F[2]])
            elif (fX < F[0]) and (fX > F[1]):
                X = np.array([x, X[1], X[2]])
                F = np.array([fX, F[1], F[2]])
        
        pom = np.array([1, 1, 1]).transpose()
        Y = np.array([pom, X, X*X]).transpose()
        F = np.linspace(0, 0, len(X))

        for i in range(len(X)):
            F[i] = func(X[i])

        abc = np.linalg.solve(Y, F)
        x = -abc[1]/(2*abc[2])
        fX = func(x)

        n += 1

    return x, fX, n

def func(x):
    return x**2 + np.sin(x)

tol = 0.0001
xOpt, fOpt, n = parabola(-1, -0.5, tol)
print(xOpt, fOpt, n)       
