import pandas as pd

# Load the simulated exit poll data
df = pd.read_csv('data/exit_poll_data.csv')

# Stratified sampling: ensure proportional representation for gender, age, and region
from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df, test_size=0.2, stratify=df[['Gender', 'Age', 'Region']])

# Save the stratified sampled data to a new CSV file
df_train.to_csv('data/stratified_exit_poll_data.csv', index=False)

print("Stratified sample generated and saved!")
