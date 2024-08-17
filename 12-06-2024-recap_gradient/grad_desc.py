import numpy as np
from time import sleep

def diff_ax(f, point, ax, delta):
    if ax == 'x':
        return (f(point[0] + delta, point[1]) - f(point[0], point[1]))/delta
    if ax == 'y':
        return (f(point[0], point[1] + delta) - f(point[0], point[1]))/delta

def gradient(f, point, delta):
    d_fx = diff_ax(f, point, 'x', delta)
    d_fy = diff_ax(f, point, 'y', delta)
    grad = np.array([d_fx, d_fy])
    return grad

def func(x,y): # point = [x, y]
    return x**2 + y**2

point = [5,4]
delta = 0.001
step = 0.01
epsilon = 1
point_prev = point
while epsilon > 0.0001:
    point_prev = point
    grad = gradient(func, point, delta)
    point = point - step*grad
    print(f'point = {point}, f(x,y) = {func(point[0],point[1])}')
    epsilon = abs(func(point[0], point[1]) - func(point_prev[0], point_prev[1]))
    sleep(0.1)
