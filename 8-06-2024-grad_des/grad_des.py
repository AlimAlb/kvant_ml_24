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
    grad = np.array([dx,dy]) # numpy array
    return grad

point = np.array([10,3])
step = 0.01
epsilon = 100
prev_point = point
while epsilon > 0.0001:
    prev_point = point
    grad = gradient(func, point, 0.01)
    point = point - grad*step 
    print(f'point: {point}, f(x,y): {func(point[0], point[1])}')
    epsilon = abs(func(point[0], point[1]) - func(prev_point[0], prev_point[1]))


