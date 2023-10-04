str = input('Введите строку: ')
element = input('Введите символ который хотите найти: ')
total_element = 0
for i in str:
    if i == element:
        total_element +=1
    else:
        print(total_element)
        break