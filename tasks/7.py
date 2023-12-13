# Программа удаляет все вхождения введенного
# пользователем элемента из списка.

numbers: list = [3, 3, 2, 1, 5, 3, 8, 11]
num: int = int(input('Укажите элемент для удаления: '))

if not numbers:
    print('Пустой список')
elif num not in numbers:
    print('Не найден')
else:
    print([el for el in numbers if el != num])
