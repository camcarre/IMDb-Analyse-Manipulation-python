import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import nltk

print("Vérification réussie ! Tout est bien installé.")

data = pd.read_csv('IMDB Dataset.csv')

data_sorted = data.sort_values(by='review')

duplicates = data_sorted.duplicated()

print("Nombre de doublons :", duplicates.sum())
print(data_sorted[duplicates])