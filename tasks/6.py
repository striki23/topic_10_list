import random

# Программа удаляет повторяющиеся элементы из списка,
# оставляя только уникальные.

# nums: list[int] = [11, 1, 22, 33, 14, 0, 13, 22, 11, 22, 9, 33]
# Список 30 случайных чисел в диапазоне от 1 до 10
nums: list[int] = [random.randint(1, 10) for _ in range(30)]

print(f'ID: {id(nums)} Список: {nums}')
i = 0
seen: set[int] = set()
while i < len(nums):
    if nums[i] in seen:
        del nums[i]
    else:
        seen.add(nums[i])
        i += 1  # Опечатался в счетчике. Исправлено!

print(f'ID: {id(nums)} Список: {nums}')
