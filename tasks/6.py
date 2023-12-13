# Программа удаляет повторяющиеся элементы из списка,
# оставляя только уникальные.

lst = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]

# var 1
new_lst = []
for el in lst:
    if el not in new_lst:
        new_lst.append(el)
print(new_lst)

# var 2 (не упорядоченный список!)
print(list(set(lst)))
