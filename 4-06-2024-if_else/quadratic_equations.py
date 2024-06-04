# Пользователь вводит коэф-ты a, b, c квадратного уравнения
# ax^2 + bx + c = 0

# Задача: найти корни, если они существуют

# x^2 -5x + 6

#D > 0
# D = 5^2 - 4*1*6 = 25-24 = 1
# sqrtD = 1

# x1 = (-(-5) + 1)/2 = 3
# x2 = (-(-5) -1)/2 = 2

# D = 0
# Один корень

# D < 0 
# корней нет 

from math import sqrt

a_s = input()
a = int(a_s)

b_s = input()
b = int(b_s)

c_s = input()
c = int(c_s)

D = b**2 - 4*a*c

if D < 0:
    print("Нет корней")
else:   
    if D == 0:
        x = -b/(2*a)
        print("Единственный корень равен:")
        print(x)
    else: 
        sqrtD = sqrt(D)
        x1 = (-b - sqrtD)/(2*a)
        x2 = (-b + sqrtD)/(2*a)
        print("Первый корень:")
        print(x1)
        print('Второй корень')
        print(x2)        
        
# x1 = (-b+0)/2a = -b/2a
# x2 = (-b-0)/2a = -b/2a

# x^2 - 2x + 10
# x^2 -2x + 1