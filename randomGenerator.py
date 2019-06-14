import random

print("Insert Range to generate numbers, in format 'a b'. ")
x, y = input().split()


z = [random.randint(int(x), int(y)) for i in range(int(y) - int(x))]
a = ""

for i in z:
    a += str(i) + '\t'

print("\n\n" + a + "\n\n")

f = open("num.txt", "w")
f.write(a)
f.close()