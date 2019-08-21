import matplotlib.pyplot as plt
import numpy as np
import math

def f(teta, w, t):
    gl = 9.81/2
    return(-gl*teta)

def euler():
    #h, k1a, k1b, k2a, k2b, theta, omega, t;
    result1 = []        # x
    result2 = []        # y = angulo
    result3 = []        # y = velocidade

    h = 0.01
    n = 800
    teta = 0            # angulo inicial
    w = 1               # velocidade inicial
    t = 0               # tempo inicial

    for i in range(1, n + 1):
        k1a = h*w
        k1b = h*f(teta, w, t)

        k2a = h*(w + k1a)
        k2b = h*f(teta+k1a, w+k1b, t+h)

        teta += (k1a + k2a)/2
        w += (k1b + k2b)/2
        t += h

        result1.append(t)
        result2.append(teta)
        result3.append(w)
    return result1, result2, result3

r1, r2, r3 = euler()

plt.plot(r1, r2)
plt.plot(r1, r3, 'red')
plt.show()
