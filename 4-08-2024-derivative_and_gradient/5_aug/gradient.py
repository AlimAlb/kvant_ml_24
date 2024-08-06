import numpy as np 

def diff_ax(func, point, ax, delta):
    if ax == 'x':
        return (func(point[0] + delta, point[1]) - func(point[0], point[1]))/delta
    elif ax == 'y':
        return (func(point[0], point[1]+ delta) - func(point[0], point[1]))/delta

def func(x, y):
    return x**2 + y**2

def gradient(func, point, delta):
    dx = diff_ax(func, point, 'x', delta)
    dy = diff_ax(func, point, 'y', delta)
    grad = np.array([dx,dy])
    return grad

grad = gradient(func, [1,2], 0.01)
minus_grad = -grad
small_grad = grad*0.1
print(grad)
print(minus_grad)
print(small_grad)
