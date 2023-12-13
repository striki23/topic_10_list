# Программа преобразует строку с полным ФИО
# в строку с инициалами имени и отчества + фамилия

full_name: list[str, ...] = input('Введите ФИО: ').split()
fio: str = f'{full_name[1][0]}.{full_name[2][0]}. {full_name[0]}'
print(fio)
