import random

# на вход которой подаётся список чисел одной строкой.
# Программа для каждого элемента выводит  сумму двух его cоседей.

# nums: list[int, ...] = list(map(
#     int, input('Введите числа через пробел: ').split())
# )

# Список 5 случайных чисел в диапазоне от 1 до 100
nums: list[int] = [random.randint(1, 100) for _ in range(5)]
print('Исходный список:', nums)

length = len(nums)

# Вариант 1: Обычный итератор
result: list[int] = []
for i in range(length):
    left_neighbor: int = nums[i - 1]
    right_neighbor: int = nums[(i + 1) % length]
    two_sum: int = left_neighbor + right_neighbor

    result.append(two_sum)

# ----------------------------------

# Вариант 2: в одну строчку
# if length == 1:
#     print(*nums)
# else:
#     nums: list[int] = [nums[i - 1] + nums[(i + 1) % length]
#                        for i in range(length)]
#     print(*nums)
