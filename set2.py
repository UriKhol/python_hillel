set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
set3 = {3, 4, 5, 6}

print('Задача 2')
print(set1 & set2 & set3)
print()

print('Задача 3')
print(set1 - set2 - set3)
print()

print('Задача 4')
print(set1 | set2 | set3)
print()

print('Задача 5')
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)
print()

print('Задача 6')
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
print()

print('Задача 7')
print(set1.symmetric_difference(set2))
print()

print('Задача 8')
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)
print()

print('Задача 9')
set1 = {10, 20, 30, 40, 50}
set1.difference_update([10, 20, 30])
print(set1)
print()

print('Задача 11')
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(not set1.isdisjoint(set2))
if not set1.isdisjoint(set2):
    print(set1.intersection(set2))
print()

print('Задача 12')
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set1.update(set2)
print(set1)
print()

print('Задача 13')
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.difference_update(set1.intersection(set2))
print(set1)

