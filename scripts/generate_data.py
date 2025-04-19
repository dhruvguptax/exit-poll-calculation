import numpy as np
import pandas as pd

# Simulate exit poll data
np.random.seed(42)

# Define categories for demographics
genders = ['Male', 'Female', 'Other']
ages = ['18-34', '35-54', '55+']
regions = ['North', 'South', 'East', 'West']
candidates = ['Candidate A', 'Candidate B', 'Candidate C']

# Number of responses
n_responses = 1000

# Generate random data for voters
data = {
    'Gender': np.random.choice(genders, n_responses),
    'Age': np.random.choice(ages, n_responses),
    'Region': np.random.choice(regions, n_responses),
    'Voted For': np.random.choice(candidates, n_responses, p=[0.45, 0.45, 0.10])
}

df = pd.DataFrame(data)

# Save the data to a CSV file in the data/ folder
df.to_csv('data/exit_poll_data.csv', index=False)

print("Exit poll data generated and saved!")
