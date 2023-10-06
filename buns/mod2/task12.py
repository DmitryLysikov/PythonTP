phone_number = input('Введите свой номер телефона: ')
new_phoneNumber = ''
for char in phone_number:
    if char == ' ' or char == ')' or char == '(' or char == '-':
        print(new_phoneNumber, end ='')
        new_phoneNumber = ''
    else:
        new_phoneNumber += char
print(new_phoneNumber)
