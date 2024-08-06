# x^2 - 5x + 6 = 0

# D = 5^2 - 4*1*6 = 1 > 0
# x = (5 +- 1)/2 => x1 = 3, x2 = 2

# ax^2 + bx + c = 0

from math import sqrt

print('Введите коэффициент а: ')
a = input()
a_int = int(a)

print('Введите коэффициент b: ')
b = input()
b_int = int(b)

print('Введите коэффициент c: ')
c = input()
c_int = int(c)

D = b_int**2 - 4*a_int*c_int
sqrt_D = sqrt(D)

x1 = (-b_int - sqrt_D)/(2*a_int)
x2 = (-b_int + sqrt_D)/(2*a_int)

print('Первый корень: ')
print(x1)
print('Второй корень: ')
print(x2)


