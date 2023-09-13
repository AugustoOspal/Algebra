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

def sort_moudulo(ecuaciones):
    """Ordena la matriz de ecuaciones por orden de modulo"""
    counter = 0
    modulos = []
    for ecuacion in ecuaciones:
        modulos.append(ecuacion[1])
    modulos.sort(reverse=True)
    

    # Esto se puede mejorar eliminando la fila en ecuaciones cada vez que
    # la ubico en ecuaciones_sorted
    ecuaciones_sorted = []
    for i in range(len(ecuaciones)):
        for j in range(len(ecuaciones)):
            if ecuaciones[j][1] == modulos[i]:
                ecuaciones_sorted.append(ecuaciones[j])
                
    return ecuaciones_sorted

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

    ecuaciones = sort_moudulo(ecuaciones)

    # Modulo de la solucion
    M = 1
    for i in range(len(modulos)):
        M *= modulos[i]

    # Esto todavia se puede mejorar un monton
    x_i = []
    for i in range(len(ecuaciones)):
        x = []
        for j in range(M // ecuaciones[i][1]):
            n = ecuaciones[i][1] * j + ecuaciones[i][0]
            if i == 0:
                x_i.append(n)
            elif n in x_i:
                x.append(n)
        if i != 0:
            x_i = list(set(x_i) & set(x))

    return x_i[0], M


# Main
ecuaciones = []

# Ingreso de datos
numero_ecuaciones = algebra.get_int("Numero de ec: ")

if numero_ecuaciones == 0:
    exit()

print("\nx = a(mod b)\n")

# Almaceno los datos en una matriz
for i in range(numero_ecuaciones):
    ecuacion = []
    ecuacion.append(algebra.get_int("a: "))
    ecuacion.append(algebra.get_int("b: "))

    print()

    ecuaciones.append(ecuacion)

solucion, modulo = solve_chino(ecuaciones)
print("\nx = " + str(solucion) + "(mod " + str(modulo) + ")")