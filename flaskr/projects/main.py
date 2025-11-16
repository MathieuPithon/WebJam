import random
from pyscript import document
# from utils.constants import COLORS

COLORS = {
            "ROUGE": "#FF6B6B",
            "BLEU": "#4ECDC4", 
            "VERT": "#45B7D1",
            "JAUNE": "#FFE66D",
            "ORANGE": "#FF9A76",
            "VIOLET": "#9B5DE5"
        }

def random_color():
    print("Génération d'une couleur aléatoire...")
    nom_couleur, valeur_hex = random.choice(list(COLORS.items()))
    button = document.getElementById("color-btn")
    color_label = document.getElementById("color-name")
     # Appliquer la nouvelle couleur
    button.style.backgroundColor = valeur_hex
    
    # Mettre à jour l'affichage du nom
    color_label.textContent = f"Couleur actuelle: {nom_couleur}"