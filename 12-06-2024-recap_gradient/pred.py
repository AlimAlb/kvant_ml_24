import numpy as np

weights = [-0.25147984, 0.54673468]

data = np.array([
   [5, 14, 12, 2, 39, 25, 40, 15, 20, 33], # расстояние до центра в км
   [70, 120, 30, 75, 35, 100, 125, 80, 90, 78], # площадь в кв метрах
   [30, 60, 10, 35, 5, 50, 80, 40, 45, 15] # цена в миллионах
])


def lin_reg(weights, data): # weights = [w1, w2], data = [x, y]
    return weights[0]*data[0] + weights[1]*data[1]

for i in range(len(data[0])):
    print(f'prediction: {lin_reg(weights, [data[0][i], data[1][i]])}, real price: {data[2][i]}')
