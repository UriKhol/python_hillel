# 1
dictlst = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
res = []
for dict in dictlst:
    res.append((dict['color'], dict['value']))
print(res)

# 2
a_dictionary = {"a": 1, "b": 2, "c": 3}
res = []
for item in a_dictionary.items():
    res.append(item)
print(res)

# 3
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = []
for i in range(len(list_a)):
    list_c.append((list_a[i], list_b[i]))
print(list_c)

# 4
dict = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
res = tuple(dict[i] for i in range(1, 4))
print(res)

# 5
lst = ["bar", "baz", "qux", "etc"]
res = ("foo",)
for el in lst:
    res += (el,)
print(res)