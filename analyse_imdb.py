import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import Counter

# Charger les données
filename = "IMDB Dataset.csv"  # Remplace par ton chemin de fichier si nécessaire
data = pd.read_csv(filename)

# Fonction alternative de nettoyage du texte (sans NLTK)
def clean_text_simple(text):
    text = text.lower()  # Convertir en minuscule
    text = re.sub(r'\W+', ' ', text)  # Supprimer la ponctuation et caractères spéciaux
    words = text.split()  # Tokenisation simple en séparant par espaces
    return words

# Séparer les critiques positives et négatives
positive_reviews = data[data['sentiment'] == 'positive']['review'].tolist()
negative_reviews = data[data['sentiment'] == 'negative']['review'].tolist()

# Extraction des mots des critiques (limité à 1000 critiques pour performances optimales)
positive_words = []
negative_words = []

for review in positive_reviews[:1000]:
    positive_words.extend(clean_text_simple(review))

for review in negative_reviews[:1000]:
    negative_words.extend(clean_text_simple(review))

# Calcul de la fréquence des mots
positive_freq = Counter(positive_words)
negative_freq = Counter(negative_words)

# Sélection des 15 mots les plus fréquents
top_positive_words = positive_freq.most_common(15)
top_negative_words = negative_freq.most_common(15)

# Création des DataFrames pour les graphiques
df_positive = pd.DataFrame(top_positive_words, columns=['Word', 'Frequency'])
df_negative = pd.DataFrame(top_negative_words, columns=['Word', 'Frequency'])

# Création des graphiques
plt.figure(figsize=(14, 6))

# Graphique des mots positifs
plt.subplot(1, 2, 1)
sns.barplot(x='Frequency', y='Word', data=df_positive, palette="Blues_r")
plt.title('Mots les plus fréquents dans les critiques positives')
plt.xlabel('Fréquence')
plt.ylabel('Mots')

# Graphique des mots négatifs
plt.subplot(1, 2, 2)
sns.barplot(x='Frequency', y='Word', data=df_negative, palette="Reds_r")
plt.title('Mots les plus fréquents dans les critiques négatives')
plt.xlabel('Fréquence')
plt.ylabel('Mots')

# Affichage des graphiques
plt.tight_layout()
plt.show()