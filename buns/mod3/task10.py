size = int(input("Введите размерность матрицы: "))
matrix = []
for i in range(size):
    row = [i+1 for j in range(size)]
    matrix.append(row)
transposed_matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]
print("Исходная матрица:")
for row in matrix:
    print(row)
print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)
