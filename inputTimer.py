import time

def readTime():
    start_time = time.time()
    line = input()
    elapsed_time = time.time() - start_time
    retorno = "{0:.2f}".format(elapsed_time)
    return ("\n%s" % (retorno))

print("\nPRESS ENTER")
c = input()
while (True):
    lista = []
    for i in range(1, 11):
        print(i)
        t = readTime()
        lista.append(t)
    for elem in lista:
        print(elem, end = "")
    print("\nPRESS ENTER TO CONTINUE READING")
    print("_______________________________")
    c = input()

