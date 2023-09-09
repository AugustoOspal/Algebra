import algebra
import math

restos = []
cocientes = []

lineas = []

numero1 = algebra.get_int("Numero 1: ")
numero2 = algebra.get_int("Numero 2: ")

resto = 1

while resto != 0:

    linea = []

    if numero2 > numero1:
        numero1, numero2 = numero2, numero1

    cocientes.append(math.floor(numero1 / numero2)) 
    resto = numero1 % numero2
    restos.append(resto)

    linea.extend([numero1, numero2, cocientes[-1], resto])
    lineas.append(linea)

    print(f"{numero1} = {numero2} * {cocientes[-1]} {algebra.signo(resto)} {abs(resto)}")

    numero1 = numero2
    numero2 = resto

mcd = restos[-2]

resto_despejado = []
for linea in lineas[-2::-1]:
    resto_despejado.append([linea[3], linea[0], -linea[2], linea[1]])

#simepre la cantidad de veces del resto al principio va a ser 1
resto_despejado[0][0] = 1

for i in range(len(resto_despejado) - 1):
    resto_despejado[0][-1] = resto_despejado[1][1::]
    resto_despejado[0][0] = resto_despejado[0][0] + resto_despejado[0][2] * resto_despejado[0][3][1]
    resto_despejado[0][3] = resto_despejado[0][3][0]
    resto_despejado[0][0], resto_despejado[0][2] = resto_despejado[0][2], resto_despejado[0][0]
    resto_despejado[0][1], resto_despejado[0][3] = resto_despejado[0][3], resto_despejado[0][1]
    del resto_despejado[1]

print(resto_despejado[0])


#Imprimo la combinacion lineal
if resto_despejado[0][2] < 0:
    print(f"{mcd} = {resto_despejado[0][0]} * {resto_despejado[0][1]} - {-resto_despejado[0][2]} * {resto_despejado[0][3]}")

else:
    print(f"{mcd} = {resto_despejado[0][2]} * {resto_despejado[0][3]} - {-resto_despejado[0][0]} * {resto_despejado[0][1]}")