import pandas as pd
filename = "IMDB Dataset.csv"

def count_total_reviews(file):
    try:
        data = pd.read_csv(file)
        
        if 'review' in data.columns:
            total_reviews = len(data)
            print(f"Nombre total de commentaires : {total_reviews}")
        else:
            print("ERREUR : La colonne 'review' est introuvable dans le dataset.")
    
    except FileNotFoundError:
        print(f" ERREUR : Le fichier '{file}' est introuvable. Assurez-vous qu'il est dans le bon dossier.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
count_total_reviews(filename)
