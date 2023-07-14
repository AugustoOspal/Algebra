import algebra
from time import sleep
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

pol1.clear_pol()
pol2.clear_pol()

pol1.get_pol({5:-6, 2:3, 1:-9, 0:1})
pol2.get_pol({1:3, 0:2})
pol1.print_pol()
pol2.print_pol()
# pol1.dividir(pol2)
pol1.print_pol()

pol3 = algebra.Polinomio()
pol3.random_pol(4, 0, 10)
pol3.print_pol()
pol3.multiplicar(3)
pol3.print_pol()