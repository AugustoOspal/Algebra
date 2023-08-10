lista = [1, 2, 3, 4, 5]

for i in lista:
    for j in lista:
        if (i - j) % 3 == 0:
            print(f"({i}, {j})") 