counter = -20
while True: 
    if counter != -1:
        if (counter ** 2 + 3) % (counter + 1) == 0:
            print(counter)

    counter += 1