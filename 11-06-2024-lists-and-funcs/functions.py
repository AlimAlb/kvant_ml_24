from math import sin

def my_func(name):
    print(f"My first function. {name} called me")

def power(number, power):
    result = number ** power
    
    return result

def add(a, b):
    res = a + b
    return res


print(sin(add(power(2, 5), power(3, 2))))

print(power(int(input()), int(input())))
