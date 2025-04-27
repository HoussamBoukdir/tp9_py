# Initialiser une liste vide pour stocker les nombres réels
nombres_reels = []

# Demander à l'utilisateur de saisir 10 nombres réels
for i in range(10):
    nombre = float(input(f"Entrez le nombre réel {i + 1} : "))
    nombres_reels.append(nombre)

# Trouver le plus grand nombre et sa position
plus_grand = max(nombres_reels)
position_plus_grand = nombres_reels.index(plus_grand) + 1  # +1 pour une position humaine (1 au lieu de 0)
print("Le plus grand nombre est :", plus_grand, "à la position", position_plus_grand)

# Trouver le plus petit nombre et sa position
plus_petit = min(nombres_reels)
position_plus_petit = nombres_reels.index(plus_petit) + 1  # +1 pour une position humaine (1 au lieu de 0)
print("Le plus petit nombre est :", plus_petit, "à la position", position_plus_petit)
