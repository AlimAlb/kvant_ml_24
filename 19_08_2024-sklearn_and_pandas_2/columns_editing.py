import pandas as pd

df = pd.read_csv('life_exp.csv')

print(df['GDP'])
print(df['GDP']/10)


#df['GDP_new'] = df['GDP']/10
df['GDP'] = df['GDP']/10

print(df[['Country', 'Year', 'GDP']])

