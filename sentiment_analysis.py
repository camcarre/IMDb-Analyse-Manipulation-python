import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

if __name__ == "__main__":
    filename = "IMDB Dataset.csv"
    data = pd.read_csv(filename)

    reviews = data['review'].tolist()

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for review in reviews:
        scores = analyze_sentiment(review)
        if scores['compound'] >= 0.05:
            positive_count += 1
        elif scores['compound'] <= -0.05:
            negative_count += 1
        else:
            neutral_count += 1

    labels = ['Positif', 'Négatif', 'Neutre']
    sizes = [positive_count, negative_count, neutral_count]
    colors = ['lightblue', 'lightcoral', 'lightgrey']

    plt.figure(figsize=(8, 6))
    plt.bar(labels, sizes, color=colors)
    plt.title('Distribution des Sentiments')
    plt.ylabel('Nombre de Critiques')
    plt.savefig('static/sentiment_distribution.png')
    plt.close()
