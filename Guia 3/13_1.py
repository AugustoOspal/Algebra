for i in range(1, 100000):
    for j in range(1, 100000):
        k = (3/float(i)) + ((float(i) + 4) / float(j))
        if k.is_integer():
            print(f"({i}, {j})")