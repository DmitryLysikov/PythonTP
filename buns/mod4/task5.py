def count_letters(filename):
    letter_count = {}

    for letter in filename:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    letter_list = list(letter_count.items())
    letter_list.sort(key=lambda x: x[1], reverse=True)
    return letter_list


filename = input('Введите имя файла').lower()
result = count_letters(filename)
for letter, count in result:
    print(f'{letter}: {count}\n')
