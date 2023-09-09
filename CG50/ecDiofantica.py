import algebra

def solucion_particular(a, b, c):
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if a*i + b*j == c:
                return i, j

print("ax+by=c")
print("a, b, c INT\n")
a = algebra.get_int("a: ")
b = algebra.get_int("b: ")
c = algebra.get_int("c: ")

if c % algebra.mcd(a, b) != 0:
    print("\nNo tiene sol")
    exit()

mcd = algebra.mcd(a, b)
a = int(a/mcd)
b = int(b/mcd)
c = int(c/mcd)

opcion = algebra.get_int("\nX_0, Y_0?\nSi = 1\nNo = 2\nOpcion: ")
while opcion != 1 and opcion != 2:
    opcion = algebra.get_int("Opcion: ")

if opcion == 2:
    x0, y0 = solucion_particular(a, b, c)

else:
    print("\nX_0, Y_0 INT")
    x0 = algebra.get_int("X_0: ")
    y0 = algebra.get_int("Y_0: ")
    if a*x0+b*y0 != c:
        print("Sol mala")
        exit()

print("(", end="")
print(x0, end="")
print(algebra.signo(b), end="")
print("k*", end="")
print(abs(b), end=", ")
print(y0, end="")
print(algebra.signo(-a), end="")
print("k*", end="")
print(abs(a), end=")")