# Вводится список городов в одну строку через пробел.
# Программа выводит первые три города с самыми длинными названиями

cities: list[str, ...] = input('Введите ваш текст: ').split()
cities_new: list[str, ...] = sorted(cities, key=len, reverse=True)
# почему не работает - cities.sort(key=len) возвращает None
print(cities_new[:3])

# Санкт-Петербург Сочи Москва Краснодар Ростов-на-Дону Воронеж