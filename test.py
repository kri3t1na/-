# Операции с логическими переменными
a = False
b = True
# Конъюнкция
if a and b:
    print('True')
else:
    print('False')
# Дезъюнкция
if a or b:
    print('True')
else:
    print('False')
# Двойное трицание и конъянкция
if not (not b and a):
    print('True')
else:
    print('False')
# Операции с цифрами
s = 1
e = 0
c = s and e
d = e or s
g = not 7
print(c, d, g)
