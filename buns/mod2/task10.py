words = input('Введите список слов: ')
new_words = ''
for char in words:
    if char == ' ':
        print(new_words[-1], end = ' ')
        new_words = ''
    else:
        new_words += char
print(new_words[-1])
