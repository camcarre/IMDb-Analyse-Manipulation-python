import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
file_path = "IMDB Dataset.csv"
df = pd.read_csv(file_path)

# Add a column for review length (number of characters)
df["review_length"] = df["review"].apply(len)

# Plot the distribution of review lengths for each sentiment
plt.figure(figsize=(10, 5))
df[df["sentiment"] == "positive"]["review_length"].hist(alpha=0.6, bins=50, label="Positive", density=True)
df[df["sentiment"] == "negative"]["review_length"].hist(alpha=0.6, bins=50, label="Negative", density=True)
plt.xlabel("Review Length (characters)")
plt.ylabel("Density")
plt.title("Distribution of Review Lengths by Sentiment")
plt.legend()
plt.show()

