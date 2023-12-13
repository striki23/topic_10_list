# Вводятся числа в одну строчку через пробел.
# Программа выводит числа, кот повторяются более 1 раза.
# Числа в выводе не должны повторятся.

nums: list[int, ...] = list(map(
    int, input('Введите числа через пробел: ').split())
)
repeated_nums: list[int, ...] = []
for num in nums:
    if nums.count(num) > 1 and num not in repeated_nums:
        repeated_nums. append(num)
print(*repeated_nums)

# 5 5 -2 3 6 8 9 7 3 6 15 26 -26 0 158 0 7
