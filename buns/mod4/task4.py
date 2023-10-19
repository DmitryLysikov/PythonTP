words = input('Введите слово: ').lower()
word = list(words)
if word == word[::-1]:
    stri = ''.join(word)
    print(f'{stri} - это полидром')
else:
    print('Это не полидром')