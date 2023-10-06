word = input('Введите сслыку: ')
k = '.'
new_word = ''
temp = ''
for i in word[::-1]:
    if i == k:
        print(new_word[::-1])
        new_word = ''
        continue
    new_word += i
print(new_word)
