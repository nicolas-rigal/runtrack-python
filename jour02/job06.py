def numbre(num):
    if num>0:
        return"positif"
    elif num<0:
        return"négatif"
    else:
        return"c'est zéro"

print(numbre(-10))
print(numbre(10))
print(numbre(0))

num=(input('choisi un numéro soit positif ou négatif et je te dirais si il l est ou non ?'))
print(numbre(num))