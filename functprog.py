def func1(list1, list2, list3):
    a = list(filter(lambda x: x % 2 == 0, list1))
    b = list(filter(lambda x: x % 2 == 1, list2))
    c = list(filter(lambda x: x % 2 == 0, list3))
    print(a)
    print(b)
    print(c)
    t = list(zip(a, b, c))
    print(t)
    l = list(map(sum, t))
    print(l)
    res = list(filter(lambda  x: x % 2 == 1, l))
    print(res)


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    func1(list_1, list_2, list_3)

