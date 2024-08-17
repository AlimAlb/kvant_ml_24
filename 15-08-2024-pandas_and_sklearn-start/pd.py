import pandas as pd

df = pd.read_csv('life_exp.csv')

print(df.head(10))

print(df.columns)
print(df.index)