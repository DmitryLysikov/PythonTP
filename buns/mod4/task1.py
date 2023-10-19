stri = input('Введите список: ')
nums = stri.split(' ')
nums.sort()
count_one = 0
count_two = 0
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        count_one += 1
    else: count_two += 1
if count_one == 0:
    print('Все числа разные')
elif count_two == 0:
    print('Все числа равны')
else:print('Есть равные и неравные числа')