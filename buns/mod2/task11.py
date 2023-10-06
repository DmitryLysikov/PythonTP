sequence = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
digits = {}
for num in sequence:
    if num in digits:
        digits[num] += 1
    else:
        digits[num] = 1
result = False
for value in digits.values():
    if value > 1:
        result = True
        break
print(result)
