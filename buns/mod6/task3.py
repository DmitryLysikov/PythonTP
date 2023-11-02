def is_armstrong_num(number):
    if 1 < number < 10:
        return False
    num_str = str(number)
    power = len(num_str)
    armstrong_sum = sum(int(digit) ** power for digit in num_str)
    return armstrong_sum == number

def get_armstrong_num(limit):
    arr = []
    num = 1
    while limit > 0:
        if is_armstrong_num(num):
            arr.append(num)
            limit -= 1
        num += 1
    return arr


for i in get_armstrong_num(8):
    print(i, end=' ')
