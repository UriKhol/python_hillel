import random

list_ = [1] + [0] * 100 + [1]
print(list_)
print()

list_2 = []
for i in range(2, 46 * 2, 2):
    list_2.append(i)
print(list_2)
print()

x = int(input("Введите число\n"))
if x in list_2:
    print("Есть в списке")
else:
    print("Нет в списке")
print()

list_3 = [2, 8, 3, 4, 3, 5, 2, 1, -1, 3, 4, 4, 5, 8, 7, 7, 5]
print(list_3)
s = 0
p = 1
for el in list_3:
    s += el
    p *= el
print("Сумма:", s)
print("Произведение:", p)
print()

print(list_3)
max_el = list_3[0]
for el in list_3:
    if el > max_el:
        max_el = el
print("Максимальный:", max_el)
print()

print(list_3)
repeated = []
for i in range(len(list_3)):
    if list_3[i] not in repeated:
        el = list_3[i]
        for j in range(i + 1, len(list_3)):
            if list_3[i] == list_3[j]:
                repeated.append(list_3[i])
                print("Есть повторение числа:", list_3[i])
                break
print()

print(list_3)
min_el_index = max_el_index = 0
for i in range(1, len(list_3)):
    if list_3[i] > list_3[max_el_index]:
        max_el_index = i
    if list_3[i] < list_3[min_el_index]:
        min_el_index = i
list_3[max_el_index], list_3[min_el_index] = list_3[min_el_index], list_3[max_el_index]
print(list_3)
print()

print(list_3)
result = []
for i in range(len(list_3) - 1, -1, -1):
    result.append(list_3[i])
print(result)
list_3.reverse()
print(list_3)