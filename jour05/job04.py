def cesar(msg="", clef=0): 
    alphabet="abcdefghijklmnopqrstuvwxyz" 
    chiffre="" 

    for l in msg.lower(): 
        pos=alphabet.find(l) 
        chiffre+=alphabet[(pos+clef) % 26] if pos != -1 else l 

    return chiffre 
  
message= input("Message à chiffré : ") 
cle = int(input("Clé de chiffrement entre 1 et 26 : "))
chiffre=cesar(message, cle) 
dechiffre=cesar(chiffre, -cle) 
print(message, "=>", "Texte déchiffré : " + chiffre, "=>", dechiffre)