import math
import random


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

    if div == 1:
        return 1

    while int(num % div) == 0:
        num = int(num / div)
        i += 1

    return i


def get_divisors(num, negativos=True, uno=True):
    # flag para negativos
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
    if num > 0:
        return "+"
    else:
        return "-"


# def resto_chino(matriz):
#     """La matriz nx3 siendo n el numero de ecuaciones"""

#     #Primero quiero ver si hay alguna ecuacion repetida, si hay la borroas


class Polinomio:
    """Crea una clase de polinomios para representar los coeficientes de cada termino y poder operar con ellos.
    El polinomio se representa como una diccionario de grados y coeficientes
    donde el grado es la clave y el coeficiente es el valor.
    Un ejemplo de polinomio seria: 2x^3 + 5x^2 + 3x + 1 se representaria como {3:2, 2:5, 1:3, 0:1}
    en orden del mayor al menor grado.
    Para obtener el polinomio se usa el metodo get_pol que utiliza un diccionario de la forma {grado: coeficiente}
    Los polinomios se pueden sumar, restar, multiplicar, dividir y derivar.
    Para sumar, restar y multiplicar se usan los metodos sumar, restar y multiplicar respectivamente.
    Para dividir se usa el metodo dividir, y devuelve el cociente y el resto.
    Para derivar se usa el metodo derivar.
    Para evaluar el polinomio en un valor se usa el metodo eval
    Para imprimir el polinomio se usa el metodo print_pol
    Para obtener el grado del polinomio se usa el metodo grado
    Para obtener el coeficiente de un termino se usa el metodo coef, con el grado del termino como argumento.
    El metodo gen_pol genera un polinomio de grado minimo usando el polinomio interpolador de Lagrange.
    tomando como argumento una lista de puntos de la forma (x, y)"""

    def __init__(self, coeficientes={0:0}):
        self.coeficientes = coeficientes

    def get_pol(self, diccionario):

        if type(diccionario) != dict:
            raise TypeError("El argumento debe ser un diccionario")

        for key in diccionario:
            if type(key) != int:
                raise TypeError("Las claves del diccionario deben ser enteros")

            self.coeficientes[key] = diccionario[key]

    def random_pol(self, grado, minimo, maximo):
        """Genera un polinomio aleatorio de grado grado con coeficientes entre minimo y maximo"""
        self.clear_pol()
        for i in range(grado + 1):
            self.coeficientes[i] = random.randint(minimo, maximo)

    def clear_pol(self):
        self.coeficientes = {}

    def add_term(self, grado, coeficiente):
        self.coeficientes[grado] = coeficiente

    def sort_pol(self, reverse=True):
        if reverse:
            self.coeficientes = dict(sorted(self.coeficientes.items(), reverse=True))
        else:
            self.coeficientes = dict(sorted(self.coeficientes.items()))

    def isMonico(self):
        if len(self.coeficientes) == 1:
            return True
        
    def grado(self):
        return max(self.coeficientes.keys())

    def print_pol(self):
        if self.coeficientes == {}:
            print("0")
            return

        pol = ""
        grado_maximo = max(self.coeficientes.keys())
        grado_minimo = min(self.coeficientes.keys())

        # Por ahora que los imprima solamente si estan ordenados, porque sino habria que cambiar
        # que se no se imprima el signo solamente si el es el coeficiente principal
        self.sort_pol()

        # No me gusta mucho como quedo esto, ver si se puede mejorar
        for key in self.coeficientes:
            if self.coeficientes[key] == 0:
                continue

            elif key == grado_maximo and abs(self.coeficientes[key]) != 1:
                pol += str(self.coeficientes[key])

            elif key == grado_maximo and self.coeficientes[key] == -1:
                pol += "-"

            elif self.coeficientes[key] != 1 or key == grado_minimo:
                pol += signo(self.coeficientes[key]) + str(abs(self.coeficientes[key]))

            if key > 1:
                pol += f"x^{str(key)}"
            elif key == 1:
                pol += "x"

        print(pol)

    def sumar(self, pol):
        if type(pol) != Polinomio:
            raise TypeError("El argumento debe ser un polinomio")

        for key in pol.coeficientes:
            if key in self.coeficientes:
                self.coeficientes[key] += pol.coeficientes[key]
            else:
                self.coeficientes[key] = pol.coeficientes[key]

    def restar(self, pol):
        if type(pol) != Polinomio:
            raise TypeError("El argumento debe ser un polinomio")

        for key in pol.coeficientes:
            if key in self.coeficientes:
                self.coeficientes[key] -= pol.coeficientes[key]
            else:
                self.coeficientes[key] = -pol.coeficientes[key]

    def multiplicar(self, pol):
        if type(pol) != Polinomio and not str(pol).isnumeric():
            raise TypeError("El argumento debe ser un polinomio")

        new_pol = Polinomio()
        new_pol.clear_pol()

        if type(pol) != Polinomio:
            pol = Polinomio({0: pol})

        for key in pol.coeficientes:
            for key2 in self.coeficientes:
                if key + key2 in new_pol.coeficientes:
                    new_pol.coeficientes[key + key2] += pol.coeficientes[key] * self.coeficientes[key2]
                else:
                    new_pol.coeficientes[key + key2] = pol.coeficientes[key] * self.coeficientes[key2]

        self.coeficientes = new_pol.coeficientes