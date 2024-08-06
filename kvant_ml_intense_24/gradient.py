import numpy as np

def diff_ax(f, point, axis, delta):
    if axis == 'x':
        return (f(point[0]+delta, point[1]) - f(point[0], point[1]))/delta
    elif axis == 'y':
        return (f(point[0], point[1]+delta) - f(point[0], point[1]))/delta

def func(x, y):
    return x**2 + y**2

def gradient(f, point, delta):
    axis_x = diff_ax(f, point, 'x', delta)
    axis_y = diff_ax(f, point, 'y', delta)
    grad = np.array([axis_x, axis_y])
    return grad

def optimize(f, point, step, stop):
    epsilon = 100000
    prev_point = point
    while epsilon > stop:
        prev_point = point
        grad = gradient(f, point, 0.001)
        point = point - grad*step
        epsilon = abs(f(point[0], point[1]) - f(prev_point[0], prev_point[1]))
    return point 



print(optimize(func, np.array([2,5]), 0.01, 0.00001))
    
