first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

if first_number < second_number < third_number:
    print("Число между двумя другими:", second_number)
elif first_number < third_number < second_number:
    print("Число между двумя другими:", third_number)
elif second_number < first_number < third_number:
    print("Число между двумя другими:", first_number)
elif second_number < third_number < first_number:
    print("Число между двумя другими:", third_number)
elif third_number < first_number < second_number:
    print("Число между двумя другими:", first_number)
elif third_number < second_number < first_number:
    print("Число между двумя другими:", second_number)