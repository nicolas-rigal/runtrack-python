n = int(input("entrez le nombre de lignes: "))
for i in range(n+1):
    for j in range(n-i):
        print(" ", end = " ")
    for j in range(i, i+i+1):
        print((i+1)%n, end = " ")
        i = i + 1
    if i>0:                    ## Partie que je n'arrive pas à coder pour que le triangle soit symétrique
        for j in range(i-1):
            i = 2*i - 2
            print((i+1) % n, end=" ")
 
    print()