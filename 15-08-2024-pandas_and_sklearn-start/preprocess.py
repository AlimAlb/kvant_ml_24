import pandas as pd

df = pd.read_csv('life_exp.csv')

# print(df)
# print()
# print(df.dropna()) # drop all NaNs (not a number)
# print(df.fillna(10))

print(df['Schooling'])
print(df['Schooling']*10)
