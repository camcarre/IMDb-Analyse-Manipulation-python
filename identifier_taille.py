import pandas as pd
df = pd.read_csv("IMDB Dataset.csv")
print("Dimensions :", df.shape) # (lignes, colonnes)
df.head(5) # Pour observer les premières lignes