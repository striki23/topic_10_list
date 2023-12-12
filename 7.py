# Программа удаляет все вхождения введенного
# пользователем элемента из списка.

lst: list = [3, 3, 2, 1, 5, 3, 8, 11]
num: int = int(input('Укажите элемент для удаления:'))
if not lst:
    print('Пустой список')
elif num not in lst:
    print('Не найден')
else:
    # var 1
    while num in lst:
        lst.remove(num)
    print(lst)

    # var 2
    # new_lst = [el for el in lst if el != num]
    # print(new_lst)
