# Вводятся числа в одну строчку через пробел.
# Программа выводит уникальные числа, сохраняя упорядоченность.

nums: list[int, ...] = list(map(
    int, input('Введите числа через пробел: ').split())
)
# uniq_nums: list[int, ...] = [num for num in nums if nums.count(num) == 1]
# print(*uniq_nums)

# 5 5 -2 3 6 8 9 7 3 6 15 26 -26 0 158 0 7
length: int = len(nums)

for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            break
    else:
        print(nums[i], end=' ')

# 90 43 5 -7 11 6 32 -1 90 43 21 6 54 5 -6
