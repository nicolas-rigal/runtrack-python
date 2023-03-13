def tapisserie(n): 
    # Le bord
    bord = "+"
    for i in range(n+1):
        bord += "-"
    bord += "+"
 # Ajout d'une ligne de retour à la ligne
    
    # La boucle d'affichage 
    print(bord)
    for i in range(n+1):
        tapis = ""
        for j in range(n-i):
            tapis += "#"
        tapis += " "
        for j in range(i):
            tapis += "#"
        print("|" + tapis + "|")
    print(bord)
    
tapisserie(5) 
#tapisserie(10)
#tapisserie(100)
