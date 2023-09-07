def mcd(num1, num2):
    """MCD calculado con algoritmo de Euclides"""
    if num2 == 0:
        return num1
    
    return mcd(num2, num1 % num2)

for i in range(1, 1000):
    for j in range(1, 1000):
        k = (3 * ((i**2) / (j**2))) - (7 * (i / j))
        if k.is_integer():
            if mcd(i, j) == 1:
                print(f"({i}, {j})")