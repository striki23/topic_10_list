#  Программа ищет определенное слово в строке,
# если слово присутствует в строке, выведите это слово и его индекс.

line = input('Введите любую строку: ')
looking_for = input('Введите слово для поиска: ')

if looking_for not in line.split():
    print(f'Слово "{looking_for}" не существует в строке "{line}"')
else:
    print(
        f'Слово "{looking_for}" существует в строке "{line}" '
        f'на позиции {line.split().index(looking_for)}'
    )
