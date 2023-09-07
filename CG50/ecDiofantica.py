def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def get_int(message):
    negative = False
    message = str(message)
    num = input(message)
    while True:
        if num[0] == '-':
            num = num[1::]
            negative = True
        if num.isdigit():
            num = float(num)
            if negative:
                num = -num
            return int(num)
        num = input(message)

def mcd(num1, num2):
    """MCD calculado con algoritmo de Euclides"""
    if num2 == 0:
        return num1
    
    return mcd(num2, num1 % num2)

def solucion_particular(a, b, c):
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if a*i + b*j == c:
                return i, j

def signo(num):
    if num > 0:
        return "+"
    else:
        return "-"

print("ax+by=c")
print("a, b, c INT\n")
a = get_int("a: ")
b = get_int("b: ")
c = get_int("c: ")

if c % mcd(a, b) != 0:
    print("\nNo tiene sol")
    exit()

mcd = mcd(a, b)
a = int(a/mcd)
b = int(b/mcd)
c = int(c/mcd)

opcion = get_int("\nX_0, Y_0?\nSi = 1\nNo = 2\nOpcion: ")
while opcion != 1 and opcion != 2:
    opcion = get_int("Opcion: ")

if opcion == 2:
    x0, y0 = solucion_particular(a, b, c)

else:
    print("\nX_0, Y_0 INT")
    x0 = get_int("X_0: ")
    y0 = get_int("Y_0: ")
    if a*x0+b*y0 != c:
        print("Sol mala")
        exit()

print("(", end="")
print(x0, end="")
print(signo(b), end="")
print("k*", end="")
print(abs(b), end=", ")
print(y0, end="")
print(signo(-a), end="")
print("k*", end="")
print(abs(a), end=")")
