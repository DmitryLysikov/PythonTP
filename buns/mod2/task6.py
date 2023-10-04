word = input('Введите сслыку: ')
k = '.'
new_word = ''
for i in word:
    if i == k:
        print(new_word)
        new_word = ''
        continue
    new_word += i
print(new_word)