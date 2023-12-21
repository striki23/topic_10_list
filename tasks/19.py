# Вводятся числа в одну строчку через пробел.
# Программа выводит числа, кот повторяются более 1 раза.
# Числа в выводе не должны повторятся.

nums = list(map(int, input('Введите числа через пробел: ').split()))
repeated_nums = []
for idx, num in enumerate(nums):
    if num in nums[idx + 1:] or num in repeated_nums:
        repeated_nums.append(num)

print(*repeated_nums)

# 1 9 7 3 6 2 7 3 4 3
length = len(nums)
for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            print(nums[i], end=' ')

# TODO: Неверный вывод.
