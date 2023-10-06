str = input('Введите строку: ')
total_vowels = 0
total_consonants = 0
vowels = {'а', 'о', 'и', 'е', 'у', 'ы', 'э', 'я', 'ё'}
consonants = {'б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'}
for i in str:
    if i.lower() in vowels:
        total_vowels += 1
    elif i.lower() in consonants:
        total_consonants += 1
print(f"Количество гласных букв: {total_vowels}")
print(f"Количество согласных букв: {total_consonants}")
