
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the stratified data
df_train = pd.read_csv('data/stratified_exit_poll_data.csv')

# Encode categorical variables
le = LabelEncoder()
df_train['Gender'] = le.fit_transform(df_train['Gender'])
df_train['Age'] = le.fit_transform(df_train['Age'])
df_train['Region'] = le.fit_transform(df_train['Region'])
df_train['Voted For'] = le.fit_transform(df_train['Voted For'])

# Define features and target
X_train = df_train[['Gender', 'Age', 'Region']]
y_train = df_train['Voted For']

# Train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save the model (using joblib)
import joblib
joblib.dump(model, 'model/exit_poll_predictor.pkl')

print("Model trained and saved!")
