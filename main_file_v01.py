# import tkinter as tk

# carte des intersections :
# 0 = intersection vide ;
# 1 = jeton joueur 1 ;
# 2 = jeton joueur 2
MAP = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


def clique_correspondance(event):
    x, y = event.x, event.y
    print(x, y)
    pass


def actualisation_graphique():
    for elm in MAP:
        if elm == 0:
            pass
            # créer intersection vide (ou ne rien creer)
        elif elm == 1:
            pass
            # créer jeton du joueur 1
        elif elm == 2:
            pass
            # créer jeton du joueur 2
    pass
