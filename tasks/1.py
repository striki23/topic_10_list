# Программа печатает каждый раз с новой строки
# элемент списка и его индекс

d: list = [15, 82, 30, 44, 10]
# d = []
if not d:
    print(False)
else:
    for index, num in enumerate(d):
        print(num, index)
