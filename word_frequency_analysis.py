import pandas as pd
import nltk
from collections import Counter
import string

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

filename = "IMDB Dataset.csv"

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return words

def get_word_frequencies(file):
    data = pd.read_csv(file)
    positive_reviews = data[data['sentiment'] == 'positive']['review'].tolist()
    negative_reviews = data[data['sentiment'] == 'negative']['review'].tolist()
    
    positive_words = []
    negative_words = []
    
    for review in positive_reviews:
        positive_words.extend(clean_text(review))
    
    for review in negative_reviews:
        negative_words.extend(clean_text(review))
    
    positive_freq = Counter(positive_words)
    negative_freq = Counter(negative_words)
    
    total_positive = sum(positive_freq.values())
    total_negative = sum(negative_freq.values())
    
    positive_percentages = {word: (count / total_positive) * 100 for word, count in positive_freq.items()}
    negative_percentages = {word: (count / total_negative) * 100 for word, count in negative_freq.items()}
    
    def categorize_frequency(freq_dict):
        high = {word: percent for word, percent in freq_dict.items() if percent > 0.5}
        medium = {word: percent for word, percent in freq_dict.items() if 0.1 <= percent <= 0.5}
        low = {word: percent for word, percent in freq_dict.items() if percent < 0.1}
        return high, medium, low
    
    high_pos, med_pos, low_pos = categorize_frequency(positive_percentages)
    high_neg, med_neg, low_neg = categorize_frequency(negative_percentages)
    
    print("Positive Words - High Frequency:", list(high_pos.keys())[:10])
    print("Positive Words - Medium Frequency:", list(med_pos.keys())[:10])
    print("Positive Words - Low Frequency:", list(low_pos.keys())[:10])
    
    print("Negative Words - High Frequency:", list(high_neg.keys())[:10])
    print("Negative Words - Medium Frequency:", list(med_neg.keys())[:10])
    print("Negative Words - Low Frequency:", list(low_neg.keys())[:10])

get_word_frequencies(filename)