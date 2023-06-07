import algebra
numero = int(input("Num: "))
for div in algebra.get_divisors(numero, negativos=False):
    print("Div: ", end="")
    print(div, end=" | ")
    print("Val = ", end="")
    print(algebra.valuacion(numero, div))