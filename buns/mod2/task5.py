alphabet = "abcdefghijklmnopqrstuvwxyz"
i = input('Введите букву от которой надо искать: ')
n = int(input('Введите шаг: '))
letter = ''
index = alphabet.index(i)
new_index = (index + n) % 26
letter += alphabet[new_index]
print(letter)