import algebra
# # diccionario = {}
# # while True:
# #     num = int(input("Grado: "))
# #     if num == 0:
# #         break
# #     diccionario[num] = int(input("Coeficiente: "))

# # pol = algebra.Polinomio(diccionario)
# # pol.print_pol()

# # pol1 = algebra.Polinomio()
# # pol2 = algebra.Polinomio()

# # pol1.clear_pol()
# # pol2.clear_pol()

# # pol1.get_pol({5:-6, 2:3, 1:-9, 0:1})
# # pol2.get_pol({1:3, 0:2})
# # pol1.print_pol()
# # pol2.print_pol()
# # # pol1.dividir(pol2)
# # pol1.print_pol()

# # pol3 = algebra.Polinomio()
# # pol3.random_pol(4, 0, 10)
# # pol3.print_pol()
# # pol3.multiplicar(3)
# # pol3.print_pol()

# for _ in range(100):
#     pol = algebra.Polinomio()
#     pol.random_pol()
#     pol.print_pol()

# matriz = [[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0],[0, 0, 0, 1, 0]]

#make a function that prints a matrix
# def print_matrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             print(matrix[i][j], end = " ")
#         print()

# print_matrix(matriz)

# total_counter = 0
# while True:
#     matriz, counter = algebra.make_sim(matriz)
#     total_counter += counter
#     counter = 0
#     matriz, counter = algebra.make_trans(matriz)
#     total_counter += counter
#     counter = 0
#     if total_counter == 0:
#         break
#     else:
#         total_counter = 0
# print_matrix(matriz)

# print(algebra.combinacion_lineal(7, -18))

p1 = algebra.Polinomio()
p2 = algebra.Polinomio()
p3 = algebra.Polinomio()
p4 = algebra.Polinomio()

p1.random_pol()
p2.random_pol()

p1.print_pol()
p2.print_pol()

p3 = algebra.sumar_pols(p1, p2)
p3.print_pol()

p4 = algebra.multiplicar_pols(p1, p2)
p4.print_pol()

p5 = algebra.Polinomio()
p5.get_pol({0:-1})

p4 = algebra.multiplicar_pols(p5, p1)
p4.print_pol()