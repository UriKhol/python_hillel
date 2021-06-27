st = {1, 7}
print(st)
st.update('hi', (34, 62, 4), [4, 6, 6, 2])
print(st)
st.add('hi')
print(st)

st.discard('hi')
print(st)
st.discard('no')
print(st)
st.remove(4)
print(st)
print()

print(st.pop())
print(st)
st.clear()
print(st)
print()

set_A = {'h', 'e', 'l', 'l', 'o'}
set_B = {'w', 'o', 'r', 'l', 'd'}
print(set_A)
print(set_B)
print()

print(set_A | set_B)
print(set_A.union(set_B))
print()

print(set_A & set_B)
print(set_B.intersection(set_A))
print()

print(set_B - set_A)
print(set_A.difference(set_B))
print()

print(set_A ^ set_B)
print(set_B.symmetric_difference(set_A))
print()

print("Не пересекаются:", set_A.isdisjoint(set_B))
print()

set_A = set()
set_A.update("Hello world")
set_B = set()
set_B.update("word")
print(set_A, '\n', set_B)
print("A содержит B:", set_A.issuperset(set_B))
print("A содержится в B:", set_A.issubset(set_B))
print()
