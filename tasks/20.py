# на вход которой подаётся список чисел одной строкой.
# Программа для каждого элемента выводит  сумму двух его cоседей.

nums: list[int, ...] = list(map(
    int, input('Введите числа через пробел: ').split())
)
if len(nums) == 1:
    print(*nums)
else:
    new_nums: list[int, ...] = []
    for i, num in enumerate(nums):
        if i == 0:
            x_num = nums[i+1] + nums[len(nums)-1]
        elif i == len(nums) - 1:
            x_num = nums[i - 1] + nums[0]
        else:
            x_num = nums[i - 1] + nums[i + 1]

        new_nums.append(x_num)

    print(*new_nums)
