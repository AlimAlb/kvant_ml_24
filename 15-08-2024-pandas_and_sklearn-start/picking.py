import pandas as pd
df = pd.read_csv('life_exp.csv')

print(df.iloc[0])
print()
print(df.iloc[10])
print()
print(df.iloc[100])
print()
print(df.iloc[[1,5,10]])
print(df.iloc[0]['Country'])

