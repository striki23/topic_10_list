# Пользователь вводит предложение(какой-либо текст).
# Программа переворачивает 1) строку и  2) строку и все слова в строке.

line: str = input('Введите ваш текст: ')

line_rev: list[str, ...] = line.split()[::-1]
line_word_rev: str = line[::-1]
print(*line_rev)
print(line_word_rev)
