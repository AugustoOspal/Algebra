import algebra

numero = 900
print(algebra.get_divisors(numero))
for divisor in algebra.get_divisors(numero):
    print(algebra.valuacion(numero, divisor))