import pandas as pd
from sklearn.linear_model import Ridge

df = pd.DataFrame({
    'Area': [90, 120, 70, 60, 30],
    'Distance': [5, 15, 25, 3, 10],
    'Price': [100, 50, 10, 25, 30]
})

reg = Ridge()
Y = df['Price']
X = df[['Area', 'Distance']]
reg.fit(X, Y)
print(reg.coef_)
print(reg.predict([[70, 5]]))

