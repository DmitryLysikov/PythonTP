sequence = input('Введите последовательность чисел через пробел: ').split()
sequence = [int(num) for num in sequence]
print(True) if len(sequence) == len(set(sequence)) else print(False)


