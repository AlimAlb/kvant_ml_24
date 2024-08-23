import pandas as pd

df = pd.read_csv('car_price.csv')

print(df.aggregate({
    'horsepower': 'max',
    'price': 'mean',
    'peakrpm':'min'
}))
print()
print(df['horsepower'].max())
print(df['price'].mean())
print(df['peakrpm'].min())