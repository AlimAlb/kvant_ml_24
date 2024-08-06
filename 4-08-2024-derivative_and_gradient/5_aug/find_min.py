def diff(f, x, delta):
    return (f(x + delta) - f(x))/delta

def func(x):
    return x**2 -2*x + 4

x = 5
step = 0.01
epsilon = 1000
x_prev = x
while epsilon > 0.0001:
    x_prev = x
    if diff(func, x, delta = 0.001) > 0:
        x -= step
    else:
        x += step
    print(f"x = {x}, f(x) = {func(x)}")
    epsilon = abs(func(x) - func(x_prev))
