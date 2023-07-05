ecuaciones = []
num_ecuaciones = int(input("Num ecuaciones: "))
for i in range(num_ecuaciones):
    ec = []
    print(f"Ec. {i + 1}: ")
    num = int(input("Num: "))
    ec.append(num)
    mod = int(input("Mod: "))
    ec.append(mod)
    ecuaciones.append(ec)

final_mod = 1
for i in range(num_ecuaciones):
    final_mod *= ecuaciones[i][1]

congruecias = []
for i in range(num_ecuaciones):
    j = 0
    congruente = []
    while ((ecuaciones[i][1] * j + ecuaciones[i][0]) <= final_mod):
        congruente.append(ecuaciones[i][1] * j + ecuaciones[i][0])
        j += 1
    
    congruecias.append(congruente)

coincidencias = 0
for i in congruecias[0]:
    for j in range(num_ecuaciones - 1):
        for z in congruecias[j]:
            if (i == z):
                coincidencias += 1
                break

    if coincidencias == num_ecuaciones:
        print(i)