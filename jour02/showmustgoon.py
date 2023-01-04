def si_triangle_realisable(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Function definition for type
def type_de_triangle(a,b,c):
    if a==b and b==c:
        print('Le Triangle est un Equilateral.')
    elif a**2+b**2==c**2 :
        print('Le Triangle est un rectragle.')
    #vérification si triangle est rectangle et isoceles non fonctionelle
    if a==b or b==c or a==c:
        print('Le Triangle est rectragle et Isosceles.')
    elif a==b or b==c or a==c:
        print('Le Triangle est Isosceles.')
    else:
        print('Le Triangle est un Scalane')

# input
side_a = float(input('Enter la taille du coté a: '))
side_b = float(input('Enter la taille du coté b: '))
side_c = float(input('Enter la taille du coté c: '))

# appelle des fonction et de la decision
if si_triangle_realisable(side_a, side_b, side_c):
    type_de_triangle(side_a, side_b, side_c)
else:
    print('Un triangle est on realisable avec ces côte.')