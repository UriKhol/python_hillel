# 1
dictlst = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
res = []
for dict in dictlst:
    res.append(tuple(dict.values()))
print(res)

# 2
a_dictionary = {"a": 1, "b": 2, "c": 3}
print(list(a_dictionary.items()))

# 3
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
print(list(zip(list_a, list_b)))

# 4
dict = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
dict.pop(4)
res = tuple(dict.values())
print(res)

# 5
lst = ["bar", "baz", "qux", "etc"]
lst.insert(0, 'foo')
print(tuple(lst))
