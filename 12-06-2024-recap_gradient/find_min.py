from time import sleep

def diff(f, x, delta):
    return (f(x+delta)-f(x))/delta

def func(x):
    return x**2 - 5*x + 6

x = 10
step = 0.001
epsilon = 1
prev_x = x

while epsilon > 0.0001:
    prev_x = x
    if diff(func, x, 0.001) > 0:
        x = x - step
    else:
        x = x + step
    print(f'x = {x}, f(x) = {func(x)}')
    epsilon = abs(func(x)-func(prev_x))
    sleep(0.001)

