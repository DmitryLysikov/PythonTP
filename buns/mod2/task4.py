number = int(input('Введите число: '))
bind = ''
octo = ''
hexe = ''

while number > 0:
    bind = str(number % 2) + bind
    number //= 2
print(bind)
number = int(input('Введите число: '))
while number > 0:
    octo = str(number % 8) + octo
    number //= 8
print(octo)
number = int(input('Введите число: '))
while number > 0:
    hexe = str(number % 16) + hexe
    number //= 16
print(hexe)