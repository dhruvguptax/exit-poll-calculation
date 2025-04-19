import pandas as pd
import joblib

# Load encoder and model
encoder = joblib.load('models/encoder.pkl')
model = joblib.load('models/model.pkl')

# New sample input (replace these values with real options from your dataset)
new_data = pd.DataFrame([{
    'Gender': 'Female',    # Must match training data
    'Age': '35-54',
    'Region': 'West'
}])

# Make sure all columns are strings (especially if categories were strings in training)
new_data = new_data.astype(str)

# Transform input
X_new_encoded = encoder.transform(new_data)

# Predict
prediction = model.predict(X_new_encoded)

print("Predicted Vote:", prediction[0])
