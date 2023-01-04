def temps(saison,type):
    if saison == "hiver" and type == "fruit" :
        return "orange, mandarine et kiwi"
    elif saison == "hiver" and type == "légume" :
        return "carotte, topinambour, endive"
    elif saison == "ete" and type == "fruit" :
        return "Poire, fraise, cassis"
    elif saison == "ete" and type == "légume" :
        return "artichaut, aubergine,navet"

#impression de toutes le possibilité possible
print(temps("ete","fruit"))
print(temps("ete","légume"))
print(temps("hiver","fruit"))
print(temps("hiver","légume"))

# teste avec input
saison=(input('ete ou hiver ?'))
type=(input('fruit ou légume ?'))
print(temps(saison,type))