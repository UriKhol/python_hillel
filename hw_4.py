import math

print("Задача 1")
a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
print("Нечётное:")
if a % 2 == 0:
    print(b)
else:
    print(a)

print("Задача 2")
a = float(input("Введите первое число\n"))
b = float(input("Введите второе число\n"))
c = float(input("Введите третье число\n"))
print("Среднее:")
if a < b < c or c < b < a:
    print(b)
if a < c < b or b < c < a:
    print(c)
if b < a < c or c < a < b:
    print(a)

print("Задача 3")
x = float(input("Введите x\n"))
y = float(input("Введите y\n"))
r = float(input("Введите радиус\n"))
if x ** 2 + y ** 2 <= r ** 2:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")

print("Задача 4")
x = float(input("Введите x\n"))
f = 0
if x > 0:
    f = 2 * x - 10
if x == 0:
    f = 0
if x < 0:
    f = 2 * abs(x) - 1
print(f)

print("Задача 5")
a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
c = int(input("Введите третье число\n"))
print("Наибольшее:")
if a < b:
    if b < c:
        print(c)
    else:
        print(b)
else:
    if a < c:
        print(c)
    else:
        print(a)

print("Задача 6")
a = int(input("Введите первую сторону\n"))
b = int(input("Введите вторую сторону\n"))
c = int(input("Введите третью сторону\n"))
if a < b + c and b < a + c and c < b + a:
    if a == b or b == c or a == c:
        if a == b == c:
            print("Равносторонний треугольник")
        else:
            print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Не треугольник")

print("Задача 7")
x = float(input("Введите x\n"))
y = float(input("Введите y\n"))
if x >= 0 and y >= 0:
    print("I четверть")
if x >= 0 and y < 0:
    print("IV четверть")
if x < 0 and y >= 0:
    print("II четверть")
if x < 0 and y < 0:
    print("III четверть")

print("Задача 8")
a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))
if a % b == 0:
    print("Делится нацело")
else:
    print("Остаток:", a % b)
print("Частное:", a // b)

print("Задача 9")
a = float(input("Введите a\n"))
b = float(input("Введите b\n"))
c = float(input("Введите c\n"))
D = b ** b - 4 * a * c
if D >= 0:
    print((-b + math.sqrt(D)) / (2 * a))
    print((-b - math.sqrt(D)) / (2 * a))
else:
    print("Нет корней")



