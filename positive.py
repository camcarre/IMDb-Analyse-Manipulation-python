import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import nltk

data = pd.read_csv("IMDB Dataset.csv")

positive_reviews = data[data['sentiment'] == 'positive']

print(f"Nombre de commentaires positifs : {len(positive_reviews)}")

print(positive_reviews.head())
