import math

def check_prime(num):
    if num > 1:
        for i in range (2, int((num/2) + 1)):
            if num % i == 0:
                return 1

    return 0

def valuacion(num, div):
    i = 0

    if div == 1:
        return 1

    while int(num % div) == 0:
        num = int(num / div)
        i += 1
        
    return i

def get_divisors(num):
    divisors = []

    i = 1
    while num != 1:
        if (not check_prime(i)) and num % i == 0:
            divisors.append(i)
            num = int(num / (i ** valuacion(num, i)))
        i += 1
    
    return divisors

def get_div_cardinal(num):
    factores = []
    divisores = get_divisors(num)
    divisores.remove(1)
    div_cardinal = 1

    for divisor in divisores:
        factores.append(valuacion(num, divisor) + 1)

    for factor in factores:
        div_cardinal *= factor

    return div_cardinal

def get_SEGCD(num, mcd, numPositiveDivisors):
    # Si se tiene el siguiente problema: El mcd entre 252 y n perteneciente a Z
    # es igual a 21. Averiguar el n mas chico posible si se sabe que n tiene
    # 24 divisores positivos.

    #SEMCD es de Smallest Equivalent Greatest Common Divisor

    i = 1
    while True:
        if (math.gcd(num, i) == mcd) and get_div_cardinal(i) == numPositiveDivisors:
            return i
        i += 1
