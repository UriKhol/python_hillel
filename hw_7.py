A = [1, 54, 123, 45, 12, 0, -1, -23, 14, -156]

print(A)
s = 0
for a in A:
    s += a
print(s)
print()

strings = ["aeceacv", "sevfwev", "1234v4bvge", "rwev5v27m78b45c", "23cdwzaxeruligv", "pwvgjwpzq]ezpf",
          "qwertyui;lkjhgf", "zxven", "nturnrfzaq", "qwecvthyj", "ewcfw", "wecfwv"]
print(strings)
c = input("Введите символ\n")
result = []
for s in strings:
    result.append(s.count(c))
print(result)
print()

list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
dig = int(input("Введите число\n"))
is_found = False
for el in list_:
    if el == dig:
        print("Число найдено")
        is_found = True
        break
if not is_found:
    print("Число не найдено")



