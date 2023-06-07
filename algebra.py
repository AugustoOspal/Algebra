import math

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
        for i in range (2, int((num/2) + 1)):
            if num % i == 0:
                return 0

    return 1

def valuacion(num, div):
    i = 0

    if div == 1:
        return 1

    while int(num % div) == 0:
        num = int(num / div)
        i += 1
        
    return i

def get_divisors(num, negativos=True, uno=True):
    #flag para negativos
    divisors = []

    num = abs(num)

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

    #SEMCD es de Smallest Equivalent Greatest Common Divisor

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

    if (div == 1):
        return 1

    while True:
        if (num % pow(div, contador) != 0):
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
            #falla esto probablemente por el [0][div]

    counter = 0
    for div in mcd:
        counter += mcd[div] * div

    return counter


def get_sigma(number):
    """Finds the divisors and the multiplicity. Returns a diccionary"""

    sigma = {}

    divisors = get_divisors(number, negativos=False)
    for div in divisors:
        sigma[div] = get_multiplicidad(number, div)

    return sigma
