# Пользователь вводит предложение.
# Программа вычисляет самое длинное и короткое слово.

line: list[str, ...] = input('Введите ваш текст: ').split()

# -----------------------var 1----------------------------
# length: list[int, ...] = [len(word) for word in line]
# # находит первое макс и мин слово (в случае если есть слова равной длины)
# word_max: str = line[length.index(max(length))]
# word_min: str = line[length.index(min(length))]

# -----------------------var 2----------------------------
word_max: str = max(line, key=len)
word_min: str = min(line, key=len)

print('Самое длинное слово в предлжении: ', word_max)
print('Самое короткое слово в предлжении: ', word_min)
