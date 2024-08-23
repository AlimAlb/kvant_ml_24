import pandas as pd

df = pd.read_csv('car_price.csv')
new_df = df[['car_ID', 'horsepower', 'price']]
print(new_df.head(10))
print()
print(new_df['price']/1000)
#new_df['price_in_thousands'] = new_df['price']/1000
print(new_df)
new_df['price'] =  new_df['price']/1000
print(new_df)
