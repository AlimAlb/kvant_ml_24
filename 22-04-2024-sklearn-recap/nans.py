import pandas as pd
import numpy as np

# NaN - not a number 

df = pd.DataFrame({
    'area': [90, np.NaN, 120, 75, np.NaN, 60, 100],
    'distance': [5, np.NaN, 10, 15, 7,np.NaN, 2],
    'price': [120, 20, np.NaN, 50, 80, 20, 15]
})

print(df)
print()
print(df.dropna())
print()
print(df.fillna(0))
print()
print(df.fillna({
    'area': df['area'].mean(),
    'distance':df['distance'].mean(),
    'price':df['price'].mean()
}))
print()
print(df.fillna(method = 'ffill'))
print()
print(df.fillna(method = 'bfill'))


