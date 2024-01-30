import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
import pickle as pk


train = pd.read_csv("Csv/Titanic/train.csv")
test = pd.read_csv("Csv/Titanic/test.csv")  
gender_submission = pd.read_csv("Csv/Titanic/gender_submission.csv")


sex_encoder = OneHotEncoder(sparse=False, drop='first')
sex_encoder = sex_encoder.fit(train[['Sex']])
sex_encoder_df_train = pd.DataFrame(sex_encoder.transform(train[['Sex']]), columns=sex_encoder.get_feature_names_out(['Sex']))
sex_encoder_df_test = pd.DataFrame(sex_encoder.transform(test[['Sex']]), columns=sex_encoder.get_feature_names_out(['Sex']))


train = pd.concat([train, sex_encoder_df_train], axis=1)
test = pd.concat([test, sex_encoder_df_test], axis=1)

print(train.head())

features = ["Pclass", "SibSp", "Sex_male"]


X_train = train[features]
X_test = test[features]

y_train = train["Survived"]


forest = RandomForestClassifier(random_state=0, max_depth=10)
forest.fit(X_train, y_train)


predictions = forest.predict(X_test)
accuracy = accuracy_score(gender_submission["Survived"], predictions)
conf_matrix = confusion_matrix(gender_submission["Survived"], predictions)
print(accuracy)
print(conf_matrix)

with open("titanic_RFC.pkl", "wb") as file:
    pk.dump(forest, file)



