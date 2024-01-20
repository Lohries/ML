import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder


data_frame = pd.read_csv('Csv/Casas.csv')


encoder = OneHotEncoder(sparse=False, drop='first')
vizinhança_encoder = encoder.fit_transform(data_frame[['Neighborhood']])
vizinhança_encoder_df = pd.DataFrame(vizinhança_encoder, columns=encoder.get_feature_names_out(['Neighborhood']))
data_frame = pd.concat([data_frame, vizinhança_encoder_df], axis=1)


X = data_frame.drop(['Price', 'Neighborhood'], axis=1)  
y = data_frame['Price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Use test_size instead of train_size

regression = LinearRegression()
regression.fit(X_train, y_train)


predictions = regression.predict(X_test)


print(predictions)
