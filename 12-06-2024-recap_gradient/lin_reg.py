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

def lin_reg(weights, data): # weights = [w1, w2], data = [x, y]
    return weights[0]*data[0] + weights[1]*data[1]

data = np.array([
   [5, 14, 12, 2, 39, 25, 40, 15, 20, 33], # расстояние до центра в км
   [70, 120, 30, 75, 35, 100, 125, 80, 90, 78], # площадь в кв метрах
   [30, 60, 10, 35, 5, 50, 80, 40, 45, 15] # цена в миллионах
])

def error(w1, w2):
    err = 0
    for i in range(len(data[0])):
        err += (lin_reg([w1, w2], [data[0][i], data[1][i]]) - data[2][i])**2
    return err

weights = np.array([1,1])
step = 0.00001
epsilon = 1
weights_prev = weights

while epsilon > 0.001:
    grad = gradient(error, weights, 0.001)
    weights = weights - step*grad
    epsilon = abs(error(weights[0], weights[1]) - error(weights_prev[0], weights_prev[1]))
    print(f'weights = {weights}, error = {error(weights[0], weights[1])}, eps = {epsilon}')
    
    sleep(0.1)










