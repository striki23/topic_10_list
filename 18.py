# Вводятся числа в одну строчку через пробел.
# Программа выводит уникальные числа, сохраняя упорядоченность.

nums: list[int, ...] = list(map(
    int, input('Введите числа через пробел: ').split())
)
uniq_nums: list[int, ...] = [num for num in nums if nums.count(num) == 1]
print(*uniq_nums)

# 5 5 -2 3 6 8 9 7 3 6 15 26 -26 0 158 0 7