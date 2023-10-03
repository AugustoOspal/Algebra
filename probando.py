import algebra

p1 = algebra.Polinomio()
p2 = algebra.Polinomio()
p3 = algebra.Polinomio()

p1.get_pol({3:2, 0:3})

for i in range(20):
    p1.multiplicar(p1)
    p1.print_pol()