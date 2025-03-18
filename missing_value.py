import pandas as pd

file_path = "IMDB Dataset.csv"
df = pd.read_csv(file_path)

missing_values = df.isnull().sum()
print(missing_values)