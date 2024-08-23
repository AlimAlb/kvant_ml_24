import pandas as pd

df = pd.read_csv('life_exp.csv')

print(df.head())

print(df.columns)

print(df[['Country', 'Year', 'Status']])

