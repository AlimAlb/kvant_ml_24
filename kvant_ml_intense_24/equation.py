# 5x + 3 = 2x - 9
# 5x - 2x = -9-3
# 3x = -12
# x = -4

# ax + b = cx + d
# ax-cx = d - b
# (a-c)x = d-b 
# x = (d-b)/(a-c)

print('введите коеффициент а уравнения: ')
a = input()
a_int = int(a)
print('введите коеффициент b уравнения: ')
b = input()
b_int = int(b)
print('введите коеффициент c уравнения: ')
c = input()
c_int = int(c)
print('введите коеффициент d уравнения: ')
d = input()
d_int = int(d)

x = (d_int-b_int)/(a_int-c_int)

print('Корень уравнения это: ')
print(x)



