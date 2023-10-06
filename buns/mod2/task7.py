str = input('Введите строку из 0 и 1: ')
one = 0
null = 0
for i in str:
    if i == '1':
        one += 1
    else:
        null += 1
if one == null:
    print('yes')
else:
    print('no')