import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

filename = "IMDB Dataset.csv"
data = pd.read_csv(filename)

reviews = data['review'].tolist()

review_counts = Counter(reviews)
top_duplicates = review_counts.most_common(15)
df_duplicates = pd.DataFrame(top_duplicates, columns=['Review', 'Count'])

plt.figure(figsize=(12, 8))
plt.barh(df_duplicates['Review'], df_duplicates['Count'], color='lightgreen')
plt.title('Phrases les plus fréquentes dans les critiques')
plt.xlabel('Nombre de Doublons')
plt.ylabel('Critiques')
plt.tight_layout()
plt.savefig('static/top_duplicates.png')  
plt.close()

print("Analyse des doublons terminée. Graphique enregistré dans 'static/top_duplicates.png'.")
