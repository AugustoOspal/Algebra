def letter_cardinal(word):
    """Funcion que le das un string y te devuelve un diccionario
    con un contador por cada letrra en el string"""
    letters = {}
    for i in word:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] += 1

    return letters

def chek_digits(dict, list):
    """Chequea que solamente esten los digitos de lista forrmando al numero"""
    for digit in dict.keys():
        if int(digit) not in list:
            return 0
        
    return 1

def check_carrdinality(dict):
    """Chequea que no esten repetidos"""
    for cardinal in dict.values():
        if cardinal != 0 and cardinal != 1:
            return 0
        
    return 1

num1 = 1200
num2 = 3522

digitos = [1, 2, 3, 4, 5, 6, 7]

counter = 0

for num in range(num1 + 1, num2):
    digits = letter_cardinal(str(num))
    if chek_digits(digits, digitos) and check_carrdinality(digits):
        counter += 1

print(counter)