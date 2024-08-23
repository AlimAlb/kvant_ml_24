import pandas as pd

df = pd.read_csv('life_exp.csv')

print(df[df['Schooling'] < 9])

print(df[(df['Schooling'] < 9) & (df['GDP'] > 2000)])