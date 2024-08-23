import pandas as pd

df = pd.read_csv('life_exp.csv')

print(df.aggregate({'GDP': 'mean', 'Schooling': 'max', 'BMI':'min'}))

print(df['GDP'].mean())
print(df['Schooling'].max())
print(df['BMI'].min())