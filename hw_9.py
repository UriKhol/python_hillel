import random

dict = {
    '1': "Jan",
    '2': "Feb",
    '3': "Mar",
    '4': "Apr",
    '5': "May",
    '6': "Jun"
}
print(dict)

dict[list(dict.keys())[0]], dict[list(dict.keys())[-1]] = dict[list(dict.keys())[-1]], dict[list(dict.keys())[0]]
dict.pop('2')
dict.update({'new_key': 'new_value'})
print(dict)

# Ответы на вопросы:
#
# student["marks"] или student.get("marks")
#
# None
#
# sample["2"][1] или sample.get("2")[1]
#
# не понимаю задания
#

cipher = {}
alphabet = []
for i in range(ord('a'), ord('z')):
    alphabet.append(chr(i))
    cipher.update({chr(i): ""})
for k in cipher.keys():
    cipher[k] = random.choice(alphabet)
    alphabet.remove(cipher[k])
print(cipher)
mes = input("Введите сообщение\n")
enc = ""
for c in mes:
    if c in cipher.keys():
        enc += cipher[c]
    else:
        enc += c
print(enc)
dec = ""
for c in enc:
    found = False
    for k in cipher.keys():
        if cipher[k] == c:
            dec += k
            found = True
            break
    if not found:
        dec += c
print(dec)
print()

dict = {}
for i in range(1, 10):
    dict.update({i: i ** 3})
print(dict)
print()

string = input("Введите строку\n")
dict = {}
for c in string:
    if c in dict.keys():
        dict[c] += 1
    else:
        dict.update({c: 1})
print(dict)
