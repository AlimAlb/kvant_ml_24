import pandas as pd

df = pd.read_csv("car_price.csv")

new_df = df[['CarName', 'fueltype', 'horsepower']]
print(new_df)
print()
print(new_df[new_df['fueltype'] == 'gas'])
print()
print(new_df[new_df['fueltype'] != 'gas'])
print()
print(new_df[new_df['horsepower'] > 100])
print()
print(new_df[(new_df['horsepower'] > 100) & (new_df['horsepower'] < 150)])
print()
print(new_df[(new_df['horsepower'] > 100) & (new_df['horsepower'] < 150) & (new_df['fueltype'] == 'diesel')])
