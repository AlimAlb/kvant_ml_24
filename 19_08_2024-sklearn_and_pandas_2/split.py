import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

df = pd.DataFrame({
    'Area': [90, 120, 70, 60, 30],
    'Distance': [5, 15, 25, 3, 10],
    'Price': [100, 50, 10, 25, 30]
})
X = df[['Area', 'Distance']]
y = df['Price']
split = train_test_split(X, y)

print(split[0])
print()
print(split[1])
print()
print(split[2])
print()
print(split[3])



