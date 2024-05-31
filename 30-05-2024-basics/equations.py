# Напишем программу для решение уравнений следующего вида: 
# ax + b = cx + d
# ax-cx = d-b
# (a-c)x = d-b
# x = (d-b)/(a-c)

a_s = input()
a = int(a_s)

b_s = input()
b = int(b_s)

c_s = input()
c = int(c_s)

d_s = input()
d = int(d_s)

x = (d-b)/(a-c)

print('Уравнение:')
print(a_s + 'x + ' + b_s + ' = ' + c_s + 'x + ' + d_s)
print()
print("Корень уравненения: ")
print(x)


