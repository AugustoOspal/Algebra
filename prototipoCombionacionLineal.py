import algebra
import math

restos = []
cocientes = []

lineas = []

numero1 = abs(algebra.get_int("Numero 1: "))
numero2 = abs(algebra.get_int("Numero 2: "))

resto = 1

if numero2 > numero1:
        numero1, numero2 = numero2, numero1

while resto != 0:

    linea = []

    cocientes.append(math.floor(numero1 / numero2)) 
    resto = numero1 % numero2
    restos.append(resto)

    linea.extend([numero1, numero2, cocientes[-1], resto])
    lineas.append(linea)

    print(f"{numero1} = {numero2} * {cocientes[-1]} {algebra.signo(resto)} {abs(resto)}")

    numero1 = numero2
    numero2 = resto

mcd = restos[-2]

#rd = resto despejado
rd = []
for linea in lineas[-2::-1]:
    rd.append([linea[3], linea[0], -linea[2], linea[1]])

#simepre la cantidad de veces del resto al principio va a ser 1
rd[0][0] = 1

for i in range(len(rd) - 1):
    rd[0][-1] = rd[1][1::]
    rd[0][0] = rd[0][0] + rd[0][2] * rd[0][3][1]
    rd[0][3] = rd[0][3][0]
    rd[0][0], rd[0][2] = rd[0][2], rd[0][0]
    rd[0][1], rd[0][3] = rd[0][3], rd[0][1]
    del rd[1]

#Imprimo la combinacion lineal
if rd[0][2] < 0:
    print(f"{mcd} = {rd[0][0]} * {rd[0][1]} - {-rd[0][2]} * {rd[0][3]}")

else:
    print(f"\n{mcd} = {rd[0][2]} * {rd[0][3]} - {-rd[0][0]} * {rd[0][1]}")