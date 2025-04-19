from sklearn.preprocessing import LabelEncoder

print("LabelEncoder works:", LabelEncoder)

le = LabelEncoder()
data = ['Male', 'Female', 'Female', 'Male']
encoded = le.fit_transform(data)

print("Encoded result:", encoded)
