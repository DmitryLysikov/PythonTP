def exponentiation(number, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exponentiation(number ** 2, n / 2)
    else:
        return number * exponentiation(number, (n - 1))


number = int(input('Введите число: '))
n = int(input('Введите степень: '))
print(exponentiation(number, n))
