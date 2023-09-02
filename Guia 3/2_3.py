counter = -20
while True: 
    if counter != 2:
        if (counter**3 - 2) % (counter - 2) == 0:
            print(counter)

    counter += 1