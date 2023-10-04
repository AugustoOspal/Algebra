import algebra

pol1 = algebra.Polinomio()
pol2 = algebra.Polinomio()

print("Para parar poner\ngrado < 0")

print("P1: ")
while True:
    grado = algebra.get_int("\nGrado: ")

    if grado < 0:
        break

    coeficiente = algebra.float(input(("Coef: "))
    pol1.insert_term(grado, coeficiente)

print("\nP2: ")
while True:
    grado = algebra.get_int("\nGrado: ")

    if grado < 0:
        break

    coeficiente = algebra.float(input(("Coef: "))
    pol2.insert_term(grado, coeficiente)

pol1.print_pol()
pol2.print_pol()

print("")

pol1 = algebra.multiplicar_pols(pol1, pol2)
pol1.print_pol()