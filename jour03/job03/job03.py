#remplace le num par un espace
for mot in range(100):
    if mot == 26:
        print("")
        continue
    elif mot == 37:
        print("")
        continue
    elif mot == 88:
        print("")
        continue
    print(mot)

#passe au num suivant

for mot in range(100):
    if mot == 26:
        mot+=1
        continue
    elif mot == 37:
        mot+=1
        continue
    elif mot == 88:
        mot+=1
        continue
    print(mot)