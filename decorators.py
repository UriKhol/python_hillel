import datetime


def run_time(func):
    def wrapped(**kwargs):
        start = datetime.datetime.now()
        result = func(**kwargs)
        print('Время выполнения:', datetime.datetime.now() - start)
        return result
    return wrapped


@run_time
def dictlist(**kwargs):
    n = kwargs['n']
    res = []
    for i in range(1, n):
        res.append({x: x**2 for x in range(i)})
    print(res)


if __name__ == "__main__":
    dictlist(n=int(input("Введите число\n")))
