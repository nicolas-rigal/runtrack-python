def DistanceForWC(marche, taille):
    totalDistance = (((taille * marche) * 2) * 7) / 100
    return print(f"En supposant que le garde aille au WC une fois par jour, il effecturas {totalDistance} métre par semaine")

nmarche = int(input("Nunbre de marche : "))
marcheTaille = int(input("Taille des marche en centimétre  : "))
DistanceForWC(nmarche, marcheTaille)