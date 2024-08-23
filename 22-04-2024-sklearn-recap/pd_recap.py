import pandas as pd

df = pd.read_csv('car_price.csv')

print(df.head(10))
print()
print(df.columns)
print()
print(df[['car_ID', 'horsepower', 'price']])