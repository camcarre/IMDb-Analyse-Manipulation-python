import pandas as pd

# Load the dataset
file_path = "IMDB Dataset.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
df.head()

print(df.head())
