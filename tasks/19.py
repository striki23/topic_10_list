import random

# Вводятся числа в одну строчку через пробел.
# Программа выводит числа, кот повторяются более 1 раза.
# Числа в выводе не должны повторятся.

# 1 9 7 3 6 2 7 3 4 3
# nums = [1, 9, 7, 3, 6, 2, 7, 3, 4, 3]
# nums = list(map(int, input('Введите числа через пробел: ').split()))

# Список 12 случайных чисел в диапазоне от 1 до 90
nums: list[int] = [random.randint(1, 90) for _ in range(12)]
print('Исходный список', nums)

length: int = len(nums)
is_found_duplicates: bool = False
for i in range(length):
    for j in range(length):
        if i != j and nums[i] == nums[j]:
            print(nums[i], end=' ')
            is_found_duplicates = True
            break

if not is_found_duplicates:
    print('В списке нет повторяющихся чисел')
