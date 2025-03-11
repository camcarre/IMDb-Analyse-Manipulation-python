import pandas as pd
import random

filename = "IMDB Dataset.csv"

def get_random_reviews(file, n=10):
    try:
        data = pd.read_csv(file)
        
        if 'review' in data.columns:
            random_reviews = data.sample(n)
            print("Voici 10 commentaires aléatoires :")
            print(random_reviews[['review', 'sentiment']])
        else:
            print("ERREUR : La colonne 'review' est introuvable dans le dataset.")
    
    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{file}' est introuvable. Assurez-vous qu'il est dans le bon dossier.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

print("Sélection de 10 commentaires aléatoires...")
get_random_reviews(filename)

