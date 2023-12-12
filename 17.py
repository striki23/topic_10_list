# Вводятся числа в одну строчку через пробел.
# Программа выводит числа, которые больше предыдущего элемента.

nums: list[int, ...] = list(map(
    int, input('Введите числа через пробел: ').split())
)
lst: list[int, ...] = []
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        lst.append(nums[i])
print(*lst)

# 5 4 2 9 3 1 6 8
