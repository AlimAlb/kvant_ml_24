import pandas as pd

df = pd.read_csv('life_exp.csv')

new_df = df[df['Country'] == 'Afghanistan']
print(new_df)
new_df = df[df['Country'] != 'Afghanistan']
print(new_df)
new_df = df[df['Schooling'] < 5]
print(new_df)
new_df = df[(df['Measles'] > 50) & (df['Measles'] < 60)]


print(new_df[['Country', 'Year', 'Measles']])


