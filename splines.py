import matplotlib.pyplot as plt
import numpy as np

def splineNat (x, a):
    n = len(x)
    h = [0] * n

    # Step 01
    for i in range(0, n - 1):
        h[i] = (x[i + 1] - x[i])

    # Step 02
    alfa = [0] * n
    for i in range(1, n - 1):
        alfa[i] = ((3/h[i]) * (a[i+1] - a[i]) - ((3/h[i - 1])*(a[i] - a[i-1])))

    # Step 03
    l = [1]
    u = [0]
    z = [0]

    # Step 04
    for i in range(1, n - 1):
        l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1])
        u.append(h[i] / l[i])
        z.append((alfa[i] - h[i-1] * z[i-1]) / l[i])

    # Step 5
    l.append(1)
    z.append(0)
    c = [0] * n
    b = [0] * n
    d = [0] * n

    # Step 6
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    return(a[:n - 1], b[:n - 1], c[:n - 1], d[:n - 1])

def splineClamp(x, a, fpo, fpn):
    n = len(x)
    h = [0] * n

    # Step 01
    for i in range(0, n - 1):
        h[i] = (x[i + 1] - x[i])

    # Step 02
    alfa = [0] * n
    alfa[0] = 3 * (a[1] - a[0]) / h[0] - (3*fpo)
    alfa[n - 1] = 3 * fpn - 3*(a[n - 1] - a[n - 2]) / h[n - 2]

    # Step 03
    for i in range(1, n - 1):
        alfa[i] = ((3/h[i]) * (a[i+1] - a[i]) - ((3/h[i - 1])*(a[i] - a[i-1])))

    # Step 04
    l = [2*h[0]]
    u = [0.5]
    z = [alfa[0] / l[0]]
    c = [0] * n
    b = [0] * n
    d = [0] * n

    # Step 05
    for i in range(1, n - 1):
        l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1])
        u.append(h[i] / l[i])
        z.append((alfa[i] - h[i - 1] * z[i-1]) / l[i])

    # Step 06
    l.append(h[n - 2] * (2 - u[n - 2]))
    z.append((alfa[n - 1] - h[n - 2]*z[n - 2]) / l[n - 1])
    c.append(z[n - 1])

    # Step 7
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j]*(c[j + 1] + 2 * c[j])/3
        d[j] = (c[j + 1] - c[j])/(3 * h[j])

    return(a[:n - 1], b[:n - 1], c[:n - 1], d[:n - 1])

def printf(var, varName):
    print(varName + ": {}".format(var) + "\n")

def readFile(file):
    x = []
    fx = []
    with open(file, "r") as fp:
        for i in fp.readlines():
            tmp = i.split(',')            
            try:
                x.append(eval(tmp[0]))
                fx.append(eval(tmp[1]))
            except:
                pass
    return(x, fx)

def functionOutput(x, fx):
    for i in range(0, len(x)):
        print('{},{}'.format(x[i], fx[i]))

x, fx = readFile("input.txt")

a, b, c, d = splineNat(x[:len(x) - 1], fx[:len(x) - 1])

a1, b1, c1, d1 = splineClamp(x[:len(x) - 1], fx[:len(x) - 1], fpo = x[len(x) - 1], fpn = fx[len(x) - 1])

# printf(a, "a")
# printf(b, "b")
# printf(c, "c")
# printf(d, "d")

# printf(a1, "a1")
# printf(b1, "b1")
# printf(c1, "c1")
# printf(d1, "d1")

varx = []
vary = []
vary1 = []

for j in range(0, len(x) - 2):
    for i in np.arange(x[j], x[j + 1], 0.02):
        
        # polinomios de spline natural        
        tmp = a[j] + b[j]*(i - x[j]) + c[j]*(i - x[j])**2 + d[j]*(i - x[j])**3
        vary.append(tmp)
        varx.append(i)
        
        # polinomios de spline fixado        
        tmp = a1[j] + b1[j]*(i - x[j]) + c1[j]*(i - x[j])**2 + d1[j]*(i - x[j])**3
        vary1.append(tmp)

plt.plot(x[:len(x) - 1], fx[:len(fx) - 1], 'x')
plt.plot(varx, vary)
plt.plot(varx, vary1)
plt.show()
