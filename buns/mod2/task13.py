str = input('Введите штрих-код: ')
even = 0
odd = 0
for i in range(len(str)):
    if i % 2 == 0:
        even += int(str[i])
    else:
        odd += int(str[i])

sum_evenOdd = even + odd * 3
if sum_evenOdd % 10 == 0:
    print('yes')
else:
    print('no')