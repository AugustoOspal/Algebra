import algebra

def check_mods(mods):
    """Dada un lista de modulos verifica que sean coprimos entre si dos a dos
    Si son todos coprimos dos a dos devuelve 0
    Si hay dos que son iguales devuelve 1
    Si hay dos que no son coprimos devuelve 2"""
    for i in range(len(mods)):
        for j in range(len(mods)):
            if i != j:
                if mods[i] == mods[j]:
                    return 1
                if algebra.mcd(mods[i], mods[j]) != 1:
                    return 2
    return 0

def solve_chino(ecuaciones):
    """Resuleve un sistema de ecuaciones de congruencia por el metodo dek resto chino
    de la forma x = a(mod b)"""
    modulos = []
    for i in range(len(ecuaciones)):
        modulos.append(ecuaciones[i][1])

    estado_modulos = check_mods(modulos)
    if estado_modulos == 1:
        print("Dos modulos iguales")
        exit()

    elif estado_modulos == 2:
        print("Dos modulos no coprimos")
        exit()

    # Modulo de la solucion
    M = 1
    for i in range(len(modulos)):
        M *= modulos[i]

    x_i = []
    for i in range(len(ecuaciones)):
        x = []
        for j in range(M // modulos[i]):
            x.append(j * modulos[i] + ecuaciones[i][0])
        x_i.append(x)
        print("x = " + str(ecuaciones[i][0]) + "(mod " + str(ecuaciones[i][1]) + ")" + " = " + str(x))

    interseccion = x_i[0]
    for i in range(1, len(x_i)):
        interseccion = list(set(x_i[i]) & set(interseccion))
        
    return interseccion[0], M



modulos = []
ecuaciones = []
numero_ecuaciones = algebra.get_int("Numero de ec: ")

print("\nx = a(mod b)\n")

for i in range(numero_ecuaciones):
    ecuacion = []
    ecuacion.append(algebra.get_int("a: "))
    ecuacion.append(algebra.get_int("b: "))

    print()

    ecuaciones.append(ecuacion)
    modulos.append(ecuacion[1])

estado_coprimos = check_mods(modulos)

if estado_coprimos:
    print("Hay dos modulos que sin iguales")
    exit()
elif estado_coprimos == 2:
    print("Hay dos modulos que no son coprimos")
    exit()
else:
    solucion, modulo = solve_chino(ecuaciones)
    print("\nx = " + str(solucion) + "(mod " + str(modulo) + ")")