phone_number = input('Введите свой номер телефона: ')
new_phoneNumber = ''.join(char for char in phone_number if char.isdigit() or char in ['+'])
print(new_phoneNumber)
