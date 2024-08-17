import numpy as np

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

grad = gradient(func, [4,5], 0.001) # [8, 10]
point = np.array([5,5])

print(grad)
print(0.01*grad)
print(point - 0.01*grad)

