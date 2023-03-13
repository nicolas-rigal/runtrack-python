def resultnotes(notes):
    arrondi=[]
    for i in notes:
        if 40.00 <= i <= 100.00:
            i+(5-i%5)
            print(i,"Bravo!!!!!!!!!!!!!")
            arrondi+=[i]
            if i+1%5==0:
                i=i+1
            elif i+2%5==0:
                i=i+2
        else:
            print("bof")
    print (arrondi)
    
notes= [8, 24, 27, 40, 48, 2, 16, 9, 7, 82, 83, 84, 85, 91]
resultnotes(notes)