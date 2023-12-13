# Программа печатает элементы списка списка через пробел
a: list = [3, 4, 5, 6, 7]
b: list = ['a', 'b', 'c', 'd']

# var 1
print(*a)

# var 2
for el in b:
    print(el, end=' ')
