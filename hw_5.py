import math

print("Задача 1")
print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Нечётное:")
if a % 2 == 1:
    print(a)
else:
    print(b)

print("Задача 2")
print("Введите первое число")
a = float(input())
print("Введите второе число")
b = float(input())
print("Введите третье число")
c = float(input())
print("Среднее:")
if a < b < c or c < b < a:
    print(b)
if a < c < b or b < c < a:
    print(c)
if b < a < c or c < a < b:
    print(a)

print("Задача 3")
print("Введите x")
x = float(input())
print("Введите y")
y = float(input())
print("Введите радиус")
r = float(input())
if x * x + y * y <= r * r:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")

print("Задача 4")
print("Введите x")
x = float(input())
f = 0
if x > 0:
    f = 2 * x - 10
if x == 0:
    f = 0
if x < 0:
    f = 2 * abs(x) - 1
print(f)

print("Задача 5")
print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Введите третье число")
c = int(input())
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
print("Введите первую сторону")
a = int(input())
print("Введите вторую сторону")
b = int(input())
print("Введите третью сторону")
c = int(input())
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
print("Введите x")
x = float(input())
print("Введите y")
y = float(input())
if x > 0:
    if y > 0:
        print("I четверть")
    else:
        print("IV четверть")
else:
    if y > 0:
        print("II четверть")
    else:
        print("III четверть")

print("Задача 8")
print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
if a % b == 0:
    print("Делится нацело")
else:
    print("Остаток:", a % b)
print("Частное:", a // b)

print("Задача 9")
print("Введите a")
a = float(input())
print("Введите b")
b = float(input())
print("Введите c")
c = float(input())
D = b ** b - 4 * a * c
if D >= 0:
    print((-b + math.sqrt(D)) / (2 * a))
    print((-b - math.sqrt(D)) / (2 * a))
else:
    print("Нет корней")



