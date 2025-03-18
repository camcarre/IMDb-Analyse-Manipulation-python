import pandas as pd

filename = "IMDB Dataset.csv"
data = pd.read_csv(filename)

data_cleaned = data.drop_duplicates()

data_cleaned.to_csv("IMDB_Dataset_Cleaned.csv", index=False)

print("Le fichier nettoyé est sauvegardé sous 'IMDB_Dataset_Cleaned.csv'")
