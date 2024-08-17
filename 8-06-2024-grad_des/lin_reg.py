import numpy as np

data = np.array([
   [5, 14, 12, 2, 39, 25, 40, 15, 20, 33], # расстояние до центра в км
   [70, 120, 30, 75, 35, 100, 125, 80, 90, 78], # площадь в кв метрах
   [30, 60, 10, 35, 5, 50, 80, 40, 45, 15] # цена в миллионах
])

weights = np.array([1,1])

def pred(x, w):
   return w[0]*x[0] +  w[1]*x[1]

def error(w1, w2):
    err = 0
    for i in range(len(data[0])):
      err += (pred([data[0][i], data[1][i]], np.array([w1, w2])) - data[2][i])**2
    return err 

def diff_ax(func, point, ax, delta):
    if ax == 'x':
        return (func(point[0] + delta, point[1]) - func(point[0], point[1]))/delta
    elif ax == 'y':
        return (func(point[0], point[1]+ delta) - func(point[0], point[1]))/delta

def gradient(func, point, delta):
    dx = diff_ax(func, point, 'x', delta)
    dy = diff_ax(func, point, 'y', delta)
    grad = np.array([dx,dy]) # numpy array
    return grad


step = 0.00001
epsilon = 100
prev_point = weights
while epsilon > 0.0001:
    prev_point = weights
    grad = gradient(error, weights, 0.01)
    weights = weights - grad*step 
    print(f'point: {weights}, f(x,y): {error(weights[0], weights[1])}')
    epsilon = abs(error(weights[0], weights[1]) - error(prev_point[0], prev_point[1]))
