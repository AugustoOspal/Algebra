import algebra
import math

restos = []
cocientes = []

lineas = []

numero1 = abs(algebra.get_int("Numero 1: "))
numero2 = abs(algebra.get_int("Numero 2: "))

if numero2 > numero1:
        numero1, numero2 = numero2, numero1

resto = 1

print()

while resto != 0:

    linea = []

    cocientes.append(math.floor(numero1 / numero2)) 
    resto = numero1 % numero2
    restos.append(resto)

    linea.extend([numero1, numero2, cocientes[-1], resto])
    lineas.append(linea)

    print(numero1, '=', numero2, '*',cocientes[-1], algebra.signo(resto), abs(resto), sep='')

    numero1 = numero2
    numero2 = resto

mcd = restos[-2]

resto_despejado = []
for linea in lineas[-2::-1]:
    resto_despejado.append([linea[3], linea[0], -linea[2], linea[1]])

#simepre la cantidad de veces del resto al principio va a ser 1
resto_despejado[0][0] = 1

print()

for i in range(len(resto_despejado) - 1):
    resto_despejado[0][-1] = resto_despejado[1][1::]
    
    print(mcd, '=', resto_despejado[0][0], '*', resto_despejado[0][1], algebra.signo(resto_despejado[0][2]), abs(resto_despejado[0][2]), '*(', resto_despejado[0][3][0], algebra.signo(resto_despejado[0][3][1]), abs(resto_despejado[0][3][1]), '*', resto_despejado[0][3][2], ')', sep='')

    resto_despejado[0][0] = resto_despejado[0][0] + resto_despejado[0][2] * resto_despejado[0][3][1]
    resto_despejado[0][3] = resto_despejado[0][3][0]
    resto_despejado[0][0], resto_despejado[0][2] = resto_despejado[0][2], resto_despejado[0][0]
    resto_despejado[0][1], resto_despejado[0][3] = resto_despejado[0][3], resto_despejado[0][1]

    """FALTA EL PRINT ESTEEEEEEEEEEEEEEEEEEEEE"""
    print(mcd, '=', resto_despejado[0][0], '*', resto_despejado[0][1], algebra.signo(resto_despejado[0][2]), abs(resto_despejado[0][2]), '*', resto_despejado[0][3], sep='')

    del resto_despejado[1]

#Imprimo la combinacion lineal
if resto_despejado[0][2] < 0:
    print("\n", mcd, '=', resto_despejado[0][0], '*', resto_despejado[0][1], '-', -resto_despejado[0][2], '*', resto_despejado[0][3], sep='')

else:
    print("\n", mcd, '=', resto_despejado[0][2], '*', resto_despejado[0][3], '-', -resto_despejado[0][0], '*', resto_despejado[0][1], sep='')