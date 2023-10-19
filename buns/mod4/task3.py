def euclids_algorithm(a, b):
    if b == 0:
        return a
    return euclids_algorithm(b, a % b)


a = int(input('Введиет первое число: '))
b = int(input('Введиет второе число: '))
print(euclids_algorithm(a, b))