# Вводятся оценки студента через пробел.
# Программа выводит инфо отчислен ли студент (больше 1 двойки)
marks: list[int, ...] = list(map(
    int, input('Введите оценки через пробел: ').split())
)
if marks.count(2) > 1:
    print('Отчислен')
else:
    print('Учится')
# 5 5 4 3 5 4 4 5 2 5 5

# Option 2
counter = 0
for mark in marks:
    if mark == 2:
        counter += 1

    if counter == 2:
        print('Отчислен')
        break
else:
    print('Учится')
