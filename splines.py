def splineNat (x, a):
    n = len(x)
    h = [0] * n

    for i in range(0, n - 1):
        h[i] = (x[i + 1] - x[i])

    print(h)

    alfa = [0] * n
    for i in range(1, n - 1):
        alfa[i] = ((3/h[i]) * (a[i+1] - a[i]) - ((3/h[i - 1])*(a[i] - a[i-1])))

    print(alfa)

    l = [1]
    u = [0]
    z = [0]

    for i in range(1, n - 1):
        l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1])
        u.append(h[i] / l[i])
        z.append((alfa[i] - h[i-1] * z[i-1]) / l[i])

    l = [1] * n
    z = [0] * n
    c = [0] * n
    b = [0] * n
    d = [0] * n

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    return(a, b, c, d)




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

print(splineNat(x, fx))
