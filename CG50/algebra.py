import math
import random

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

def factorial(num):
    if num == 1 or num == 0:
        return 1

    elif num > 1:
        return num * factorial(num - 1)

    # En caso de error devuelve 0 como unico codigo de error
    print("El numero ingresado tiene que ser positivo")
    return 0


def check_prime(num):
    if num > 1:
        for i in range(2, int((num / 2) + 1)):
            if num % i == 0:
                return 0

    return 1


def valuacion(num, div):
    i = 0

    if not check_prime(div):
        return 

    if div == 1:
        return 1

    while int(num % div) == 0:
        num = int(num / div)
        i += 1

    return i


def get_divisors(num, negativos=True, uno=True):
    # flag para negativos
    divisors = []

    num = abs(int(num))

    i = 1
    while num != 1:
        if (check_prime(i)) and num % i == 0:
            divisors.append(i)
            num = int(num / (i ** valuacion(num, i)))
        i += 1

    if negativos:
        divisores_originales = divisors.copy()

        for divisor in divisores_originales:
            divisors.append(-divisor)

    return divisors


def get_div_cardinal(num):
    """Un unico input. Pones el numero y te pone las valuaciones de sus factores"""
    factores = []
    divisores = get_divisors(num)
    divisores.remove(1)
    div_cardinal = 1

    for divisor in divisores:
        factores.append(valuacion(num, divisor) + 1)

    for factor in factores:
        div_cardinal *= factor

    return div_cardinal


def get_segcd(num, mcd, num_positive_divisor):
    """Si se tiene el siguiente problema: El mcd entre 252 y n perteneciente a Z
    es igual a 21. Averiguar el n mas chico posible si se sabe que n tiene
    24 divisores positivos."""

    # SEMCD es de Smallest Equivalent Greatest Common Divisor

    i = 1
    while True:
        if (math.gcd(num, i) == mcd) and get_div_cardinal(i) == num_positive_divisor:
            return i
        i += 1


def get_primes(num):
    """Agarra los num primeros primos en orden"""
    i = 1
    cont = 0

    primes = []

    while cont < num:
        if check_prime(i):
            primes.append(i)
            cont += 1

        i += 1

    return primes


def get_multiplicidad(num, div):
    contador = 1

    if div == 1:
        return 1

    while True:
        if num % pow(div, contador) != 0:
            return contador - 1
        contador += 1


def get_mcd(numbers):
    """Finds the gcd beetween multimple numbers"""

    mcd = {}
    divisors = {}

    for num in numbers:
        divisors[num] = get_sigma(num)

    # Puedo chequearlo de cualquir numero, porque tiene que estar en todos
    for num in divisors:
        for div in divisors[num]:
            mcd[div] = min(divisors[numbers[1]][div], divisors[num][div])
            # falla esto probablemente por el [0][div]

    counter = 0
    for div in mcd:
        counter += mcd[div] * div

    return counter

def mcd(num1, num2):
    """MCD calculado con algoritmo de Euclides"""
    if num2 == 0:
        return num1
    
    return mcd(num2, num1 % num2)

def get_sigma(number):
    """Finds the divisors and the multiplicity. Returns a diccionary"""

    sigma = {}

    divisors = get_divisors(number, negativos=False)
    for div in divisors:
        sigma[div] = get_multiplicidad(number, div)

    return sigma


def inverso_multiplicativo(num, modulo):
    """Solamente funciona si (num:modulo)|al otro numero de la congruencia"""
    i = 1
    while (num * i) % modulo != 1:
        i += 1
    return i


def ask_matriz_chino():
    """Tiene que ser en orden aX=b(mod)"""
    matriz = []
    numero_ecuaciones = int(input("Numero de ecuaciones: "))
    print("Forma: AX=B(MOD")
    for _ in range(numero_ecuaciones):
        a = int(input("\nA: "))
        b = int(input("B: "))
        mod = int(input("Mod: "))

        # Tendria que hacer algo para que si mcd != 1 lo arregle
        ecuacion = [a, b, mod]
        matriz.append(ecuacion)

    return matriz


def signo(num):
    if num >= 0:
        return "+"
    else:
        return "-"
    
def sg(num):
    if num >= 0:
        return 1
    else:
        return -1


def make_trans(matrix):
    # Dimensiones de la matriz
    # Cantidad de filas = n
    # Cantidad de columnas = m

    n = len(matrix)
    m = len(matrix[0])

    total_switch = 0
    switch_counter = 0
    while True:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    for k in range(m):
                        if matrix[j][k] == 1 and matrix[i][k] != 1:
                            matrix[i][k] = 1
                            switch_counter += 1
        if switch_counter == 0:
            break
        else:
            total_switch += switch_counter
            switch_counter = 0

    return matrix, total_switch

def make_reflex(matrix):
    """Suponiendo que es cuadrada y ordenarla. Mejorar"""
    counter = 0
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            matrix[i][i] = 1
            counter += 1
    return matrix, counter


def make_sim(matrix):
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                matrix[j][i] = 1
                counter += 1
    return matrix, counter

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False
