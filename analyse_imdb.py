import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import Counter

filename = "IMDB Dataset.csv"
data = pd.read_csv(filename)

def clean_text_simple(text):
    text = text.lower()  
    text = re.sub(r'\W+', ' ', text) 
    words = text.split() 
    return words

positive_reviews = data[data['sentiment'] == 'positive']['review'].tolist()
negative_reviews = data[data['sentiment'] == 'negative']['review'].tolist()

positive_words = []
negative_words = []

for review in positive_reviews[:1000]:
    positive_words.extend(clean_text_simple(review))

for review in negative_reviews[:1000]:
    negative_words.extend(clean_text_simple(review))

positive_freq = Counter(positive_words)
negative_freq = Counter(negative_words)

top_positive_words = positive_freq.most_common(15)
top_negative_words = negative_freq.most_common(15)

df_positive = pd.DataFrame(top_positive_words, columns=['Word', 'Frequency'])
df_negative = pd.DataFrame(top_negative_words, columns=['Word', 'Frequency'])

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.barplot(x='Frequency', y='Word', data=df_positive, palette="Blues_r")
plt.title('Mots les plus fréquents dans les critiques positives')
plt.xlabel('Fréquence')
plt.ylabel('Mots')

plt.subplot(1, 2, 2)
sns.barplot(x='Frequency', y='Word', data=df_negative, palette="Reds_r")
plt.title('Mots les plus fréquents dans les critiques négatives')
plt.xlabel('Fréquence')
plt.ylabel('Mots')

plt.tight_layout()
plt.show()