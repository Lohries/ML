import pandas as pd 
from sklearn.linear_model import LinearRegression

data_frame = pd.read_csv('Csv/Carros.csv')

X = data_frame[['Weight', 'Volume']] #Selecting colluns for training
y = data_frame['CO2'] #Trying to predict

model = LinearRegression()

model.fit(X, y)

predict = model.predict([[2300, 1300]])
print(predict)



