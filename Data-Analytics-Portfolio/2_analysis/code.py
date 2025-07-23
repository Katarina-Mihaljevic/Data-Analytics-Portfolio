import pandas as pd

# Load the dataset
df = pd.read_csv("data/DataAnalyst.csv")

# Data cleaning steps
# 1. Remove duplicate entries
df = df.drop_duplicates()

# 2. Filter out rows with missing salary values
df = df[df['Salary'].notna()]

# Save the cleaned data
df.to_csv("data/cleaned_jobs.csv", index=False)