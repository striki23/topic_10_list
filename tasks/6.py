# Программа удаляет повторяющиеся элементы из списка,
# оставляя только уникальные.

# lst = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]
#
# # var 1
# new_lst = []
# for el in lst:
#     if el not in new_lst:
#         new_lst.append(el)
# print(new_lst)
#
# # var 2 (не упорядоченный список!)
# print(list(set(lst)))

# ---------------------------------
nums: list[int] = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]
print(f'ID: {id(nums)} Список: {nums}')
i = 0
seen: set[int] = set()
while i < len(nums):
    if nums[i] in seen:
        del nums[i]
    else:
        seen.add(nums[i])
    i += 1
print(f'ID: {id(nums)} Список: {nums}')

# TODO: Посмотреть, элементы не удаляются.
