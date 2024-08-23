import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Area': [90, np.NaN, 70, np.NaN, 30],
    'Distance': [5, 15, np.NaN, 3, 10],
    'Price': [100, 50, 10, 25, 30]
})

print(df)
print()
print(df.dropna())
print()
print(df.fillna({
    'Area': df['Area'].mean(),
    'Distance': df['Distance'].mean()
}))
print()
print(df.fillna(method='bfill'))
