num = int(input("Num: "))
modulo = int(input("Modulo: "))
i = 1
while True:
    if ((num * i) % modulo == 1):
        break
    i += 1
print(i)