import pandas as pd
import numpy as np

data = np.array([
   [5, 14, 12, 2, 39, 25, 40, 15, 20, 33], # расстояние до центра в км
   [70, 120, 30, 75, 35, 100, 125, 80, 90, 78], # площадь в кв метрах
   [30, 60, 10, 35, 5, 50, 80, 40, 45, 15] # цена в миллионах
])

df = pd.DataFrame({
    'distance_to_center': data[0],
    'area': data[1],
    'price': data[2]
})

print(df)

print(df.aggregate({'distance_to_center': 'min', 'area':'max', 'price':'mean'}))