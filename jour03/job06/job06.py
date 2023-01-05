chaine="abcdefghijklmnopqrstuvwxyz" * 10 
  
for i in range(1, int((-1 + (1 + 8*len(chaine))**0.5) // 2) + 1): 
	print(chaine[:i])  
	chaine=chaine[i:]  
# for