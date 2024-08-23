import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Очень много предобработки данных

df = pd.read_csv('car_price.csv')

X = df[['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight', 'enginesize', 'boreratio', 'stroke', 'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y) # [X_train, X_test, y_train, y_test]

gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train) # обучение
result = gbr.predict(X_test)
print(f'mse for grad boosting: {mean_squared_error(y_test, result)}')

ridge = Ridge()
ridge.fit(X_train, y_train) # обучение
result = ridge.predict(X_test)
print(f'mse for ridge: {mean_squared_error(y_test, result)}')

