import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

# Load your training data
df = pd.read_csv('data/exit_poll_data.csv')  # Make sure this file exists

# Separate features and labels
X = df[['Gender', 'Age', 'Region']]
y = df['Voted For']

# OneHotEncode the features
encoder = OneHotEncoder(handle_unknown='ignore')
X_encoded = encoder.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model and encoder
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model.pkl')
joblib.dump(encoder, 'models/encoder.pkl')

print("✅ Model and encoder saved in /models/")
