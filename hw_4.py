# 1 модуль
def read_int():
    a = input("Введите целое число")
    if a.isdigit():
        print(int(a))
        return int(a)
    else:
        print("Некорректный ввод")
        return -1


def int_to_float(a):
    print(float(a))
    return float(a)


def int_to_str(a):
    print(str(a))
    return str(a)


# 2 модуль
def read_float():
    a = input("Введите дробное число")
    if not a[0].isdigit():
        print("Некорректный ввод")
        return -1.0
    has_dot = False
    for c in a:
        if c != ',' and not c.isdigit():
            print("Некорректный ввод")
            return -1.0
        if c == ',':
            if has_dot:
                print("Некорректный ввод")
                return -1.0
            else:
                has_dot = True
    print(float(a))
    return float(a)


def float_to_int(a):
    print(int(round(a)))
    return int(round(a))


def float_to_str(a):
    print(str(a))
    return str(a)


a = read_int()
b = read_float()
