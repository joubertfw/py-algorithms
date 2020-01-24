from scipy import *
import matplotlib.pyplot as plt
import math

def rungeKutta(a = 0, b = 10, N = 2000, teta = pi/4, omega = 0, l = 1):
    pos = []
    vel = []
    x = []
    px = []
    py = []
    g = 9.81
    cnt = 0
    h = (b-a)/N

    for i in range(1, N):
        x.append(cnt)
        pos.append(teta)
        vel.append(omega)

        px.append(l*sin(teta))
        py.append(-l*cos(teta))
        
        v1 = h*(-g/l*sin(teta))
        p1 = h*omega
        
        v2 = h*(-g/l*sin(teta + v1/2))
        p2 = h*(omega + p1/2)

        v3 = h*(-g/l*sin(teta + v2/2))
        p3 = h*(omega + p2/2)

        v4 = h*(-g/l*sin(teta + v3))
        p4 = h*(omega + p3)

        omega = omega + (v1 + 2*v2 + 2*v3 + v4)/6
        teta = teta + (p1 + 2*p2 + 2*p3 + p4)/6
        cnt = i*h

    return x, pos, vel, px, py

x, pos, vel, px, py = rungeKutta(a = 0, b = 10, N = 2000, teta = pi/12, omega = 0, l = 4)


plt.figure(figsize=(12,6))
plt.subplot(111),plt.plot(x, pos, 'green'),plt.xlabel('Teta (verde) - Omega (vermelho)'),plt.ylabel('')
plt.subplot(111),plt.plot(x, vel, 'red')
plt.grid(color='black', linestyle='-', linewidth = 0.2)

plt.show()
plt.figure(figsize=(12,9))
plt.subplot(312),plt.plot(px, py, 'green'),plt.xlabel('Rota do pêndulo'),plt.ylabel('')

plt.grid(color='black', linestyle='-', linewidth = 0.2)

plt.show()
