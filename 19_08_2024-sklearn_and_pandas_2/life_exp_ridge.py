import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

df = pd.read_csv('life_exp.csv')
df = df.fillna(method='ffill')
df = df.drop(['Country', 'Year', 'Status'], axis = 1)

X = df.drop('Life expectancy', axis=1)
y = df['Life expectancy']

split = train_test_split(X, y) # [X_train, X_test, y_train, y_test]
X_train = split[0]
X_test = split[1]
y_train = split[2]
y_test = split[3]

model = Ridge()

model.fit(X_train, y_train)

preds = model.predict(X_test)

for i in range(len(preds)):
    print(f'prediction: {preds[i]}, real value: {list(y_test)[i]}')