import random
from pyscript import document
from utils.constants import COLORS

def random_color():
    print("Génération d'une couleur aléatoire...")
    nom_couleur, valeur_hex = random.choice(list(COLORS.items()))
    button = document.getElementById("color-btn")
    color_label = document.getElementById("color-name")
     # Appliquer la nouvelle couleur
    button.style.backgroundColor = valeur_hex
    
    # Mettre à jour l'affichage du nom
    color_label.textContent = f"Couleur actuelle: {nom_couleur}"