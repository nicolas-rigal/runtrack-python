L = [2,4,6,8,10]
print(L[1])

def replace():
    L.insert(3, L[2] + L[4])
    L.remove(L[4])
    return(L[4])

print(replace())
print(L)