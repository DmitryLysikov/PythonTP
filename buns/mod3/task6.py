str = input('Введите слова: ').split(" ")
word_one, word_two, word_three = str[0], str[1], str[2]
print(word_one[-1] + word_two[-1] + word_three[-1])