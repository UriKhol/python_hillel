#!/usr/bin/env python
# -*- coding: utf-8 -*-
string = "как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print(string.capitalize())
print()

string = "Как Много Есть На Свете Вещей, Которые Мне Не Нужны! - СОКРАТ"
print(string)
print(string.casefold())
print()

string = "Данные загружены успешно"
print(string)
print(string.center(50, ':'))
print()

string = "Работник не справился со своими обязанностями, но не мне его судить"
print(string)
print("Количество строк 'не':", string.count("не"))
print()

string = "Hello - Привет"
print(string)
print(string.encode())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Кончается на 'Сократ':", string.endswith("Сократ"))
print()

string = "как\tмного\tесть\tна\tсвете\tвещей,\tкоторые\tмне\tне\tнужны!\t-\tСократ"
print(string)
print(string.expandtabs(1))
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Поиск строки 'меня':", string.find("меня"))
print()

string = "Он потратил ровно {days} дней и получил {dollar:.2f} долларов"
print(string)
print(string.format(days = 7, dollar=12.3))
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Индекс строки 'свет':", string.index('свет'))
print()

string = "Дело132"
print(string)
print("Только алфавит и цифры:", string.isalnum())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Только алфавит:", string.isalpha())
print()

string = '12345\u0036'
print(string)
print("Только цифры unicode:", string.isdecimal())
print()

string = '12345\u0036'
print(string)
print("Только цифры:", string.isdigit())
print()

string = "is_valid_identifier123_1"
print(string)
print("Допустимый идентификатор:", string.isidentifier())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Только маленькие буквы:", string.islower())
print()

string = "-12.6"
print(string)
print("Только цифры:", string.isnumeric())
print()

string = "Как\tмного есть на свете вещей,\nкоторые мне не нужны! - Сократ"
print(string)
print("Печатается неизменно:", string.isprintable())
print()

string = ".     "
print(string)
print("Только пробелы:", string.isspace())
print()

string = "Вещи, Которые Мне Не Нужны! - Сократ"
print(string)
print("Заголовок:", string.istitle())
print()

string = "ДОБРЫЙ ДЕНЬ123"
print(string)
print("Только большие буквы:", string.isupper())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print(":", string)
print()

string = " -> "
order = ('4', '2', '1', '5', '3')
print(order)
print(string.join(order))
print()

string = "Let's go"
print(string)
print(string.ljust(30, 'o'))
print()

string = "ХорОшИЙ дЕнЬ"
print(string)
print(string.lower())
print()

string = "1.234.ferrr1.Сократ"
print(string)
print(string.lstrip('1234fer.о'))
print()

string = "Хороший шифр"
mapping = string.maketrans('шир', 'sir', 'Хоий')
print(string)
print("Перевод:", string.translate(mapping))
print()

string = "Казнить нельзя помиловать"
print(string)
print("Деление строкой 'нельзя':", string.partition('нельзя'))
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print(string.replace('Сократ', 'Высказывание философа'))
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Поиск строки 'не' справа (rfind):", string.rfind('не'))
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Поиск строки 'не' справа (rindex):", string.index('не'))
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Деление пробелом:", string.split(' '))
print()

string = "Как много есть на свете вещей,\nкоторые мне не нужны! - Сократ"
print(string)
print("Деление строк:", string.splitlines())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print("Начинается с 'много есть':", string.startswith('много есть'))
print()

string = "512-35-15-15-address-123-124-4-5"
print(string)
print(string.strip('12345-'))
print()

string = "ХорОшИЙ дЕнЬ"
print(string)
print(string.swapcase())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print(string.title())
print()

string = "Как много есть на свете вещей, которые мне не нужны! - Сократ"
print(string)
print(string.upper())
print()

string = "1011"
print(string)
print(string.zfill(8))
print()
