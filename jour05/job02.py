def draw_rectangle(largeur,hauteur):
    c='|'+'-'*(largeur-2)+'|\n';
    print(c+ (c.replace(*'- '))*(hauteur-2) +c)

draw_rectangle(10,3)
