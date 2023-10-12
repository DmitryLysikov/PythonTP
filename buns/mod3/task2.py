num = int(input('Введите число: '))
print("Неверный ввод") if num <= 0 else (
    print(f'Двоичный: {num:b}, ' + f'Восьмеричный: {num:o}, ' + f'Шестнадцатеричный: {num:x}'))