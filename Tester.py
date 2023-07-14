import algebra
# diccionario = {}
# while True:
#     num = int(input("Grado: "))
#     if num == 0:
#         break
#     diccionario[num] = int(input("Coeficiente: "))

# pol = algebra.Polinomio(diccionario)
# pol.print_pol()

pol1 = algebra.Polinomio()
pol2 = algebra.Polinomio()

pol1.random_pol(5, -10, 10)
pol2.random_pol(5, -10, 10)

pol1.print_pol()
pol2.print_pol()

pol1.sumar(pol2)
pol1.print_pol()