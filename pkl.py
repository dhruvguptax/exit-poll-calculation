import joblib

# Load the trained model
model = joblib.load('model/exit_poll_predictor.pkl')

# If needed, check the model's features
print(model.feature_names_in_)
