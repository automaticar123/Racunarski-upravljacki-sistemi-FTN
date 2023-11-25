import numpy as np
import math

#gradf - funkcija koja racuna gradijent, x0 -pocetno pogadjanje, gamma - velicina koraka,
# epsilon - tolerancija, N - maksimalan broj koraka
def sd(gradf, x0, gamma, epsilon, N):
    x = np.array(x0).reshape(len(x0), 1) #prilagodjavanje oblika vektora/niza kako bi kod radio
    for k in range(N):
        g = gradf(x)
        x = x - gamma*g #Xk+1 = Xk - gamma*gradijent
        if np.linalg.norm(g) < epsilon: #duzina vektora manja od epsilon
            break
    return x, k+1

#omega - valjda momenat
def sdm(gradf, x0, gamma, epsilon, omega, N):
    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(shape=x.shape)
    for k in range(N):
        g = gradf(x)
        v = omega*v + gamma*g #Vk = omega*Vk-1 + gamma*gradijent
        x = x - v # Xk+1 = Xk - Vk
        if np.linalg.norm(g) < epsilon:
            break
    return x, k+1

def adam(gradf, x0, gamma, omega1, omega2, epsilon1, epsilon, N):
    x = np.array(x0).reshape(len(x0),1)
    v = np.ones(shape=x.shape)
    m = np.ones(shape=x.shape)
    for k in range(N):
        g = gradf(x)
        m = omega1*m + (1 - omega1)*g
        v = omega2*v + (1 - omega2)*np.multiply(g, g)
        m_kor = m/(1-omega1)
        v_kor = abs( v/(1-omega2))
        x = x - gamma * m_kor / np.sqrt(v_kor + epsilon1)
        #print(x)
        if(np.linalg.norm(g)<epsilon):
            break
    
    return x, k+1

# f = 1.5*x1^2 + x2^2 - 2*x1*x2 + 2*x1^3 + 0.5*x1^4
def func(x):
    return x[0]**2 + x[1]**2

# po x1 : 2*x1^3 + 6*x1^2 + 3*x1 - 2*x2
# po x2 : 2*x1 - 2*x2
def grad(x):
   x = np.array(x).reshape(np.size(x))
   return np.asarray([[2*x[0]], [2*x[1]]])

#r, it = sd(lambda x: grad(x), [2,2], 0.1, 1e-4, 100)
#r, it = sdm(lambda x: grad(x), [2,2], 0.05, 1e-4, 0.5, 100)
r, it = adam(lambda x: grad(x), [2,2], 1e-4, 0.9, 0.999, 1e-6, 1e-6,  100)
print('x opt:', r.round(2))
print('broj iteracija:',it)
print('vrednost f-je u optimumu: ',func(r))