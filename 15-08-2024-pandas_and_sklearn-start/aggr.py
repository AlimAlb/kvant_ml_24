import pandas as pd

df = pd.read_csv('life_exp.csv') # df = dataframe

#print(df.aggregate({'BMI': 'mean', 'Diphtheria': 'min', 'GDP': 'max'}))

# print(df['BMI'].mean())
# print(df['Diphtheria'].min())
# print(df['GDP'].max())

