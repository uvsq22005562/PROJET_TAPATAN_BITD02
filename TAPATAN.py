###########################
# NOMS + ROLES
###########################

###########################
# IMPORTS
import tkinter as tk

###########################
# GLOBALS VAR

MAP = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]  # 0 = vide, 1, 2 = joueur 1, 2

JETONS = [3, 3]  # jetons restant (j1, j2)

ETAT_PARTIE = 0  # 1 = placement, 2 = deplacement

TOUR_JEU = 0  # Voir c'est au tour de quel joueur

rond = []  # Liste de points de la fenêtre PvP

COORD_PTS = [
    # ligne 1
    [80, 80, 120, 120, [0, 0]],
    [380, 80, 420, 120, [0, 1]],
    [680, 80, 720, 120, [0, 2]],
    # ligne 2
    [80, 380, 120, 420, [1, 0]],
    [380, 380, 420, 420, [1, 1]],
    [680, 380, 720, 420, [1, 2]],
    # ligne 3
    [80, 680, 120, 720, [2, 0]],
    [380, 680, 420, 720, [2, 1]],
    [680, 680, 720, 720, [2, 2]]
]

COORD_LINES = [
    # ligne 1
    [130, 80, 370, 120, [[0, 0], [0, 1]]],
    [430, 80, 670, 120, [[0, 1], [0, 2]]],
    # ligne 2
    [80, 130, 120, 370, [[0, 0], [1, 0]]],
    [380, 130, 420, 370, [[0, 1], [1, 1]]],
    [680, 130, 720, 370, [[0, 2], [1, 2]]],
    # ligne 3
    [130, 380, 370, 420, [[1, 0], [1, 1]]],
    [430, 380, 670, 420, [[1, 1], [1, 2]]],
    # ligne 4
    [80, 430, 120, 670, [[1, 0], [2, 0]]],
    [380, 430, 420, 670, [[1, 1], [2, 1]]],
    [680, 430, 720, 670, [[1, 2], [2, 2]]],
    # ligne 5
    [130, 680, 370, 720, [[2, 0], [2, 1]]],
    [430, 680, 670, 720, [[2, 1], [2, 2]]]
]

COORD_DIAG = [
    # haut gauche
    [130, 130, 370, 370, [[0, 0], [1, 1]]],
    # haut droite
    [430, 130, 670, 370, [[1, 1], [0, 2]]],
    # bas gauche
    [130, 430, 370, 670, [[2, 0], [1, 1]]],
    # bas droite
    [430, 430, 670, 670, [[2, 2], [1, 1]]]
]


def window_transition(id):  # jules
    ''' ferme la fenêtre ouverte et ouvre le menu '''
    if id == 1:
        # pvp -> menu
        racine1.destroy()
        menu()
    if id == 2:
        # pv ia -> menu
        racine2.destroy()
        menu()
    if id == 3:
        # ia v ia -> menu
        racine3.destroy()
        menu()


def menu():  # thibault
    global racine
    """ Fonction qui crée:
        -une fenetre de taille 400*400
        - 4 boutons: PvP, PvIA, IAvIA et Exit
        -Exit détruit la fenetre
    """
    racine = tk.Tk()
    racine.title("Menu")
    btn_PVP = tk.Button(racine, command=game_window_1, text="Player vs Player")
    btn_PVP.pack()
    btn_PVIA = tk.Button(racine, command=game_window_3, text="Player vs IA")
    btn_PVIA.pack()
    btn_IAVIA = tk.Button(racine, command=game_window_2, text="IA vs IA")
    btn_IAVIA.pack()
    btn_quit = tk.Button(racine, command=racine.destroy, text="Quitter")
    btn_quit.pack()
    racine.mainloop()


def game_window_1():  # thibault
    global racine1, canvas
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*800
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -Utilisé pour le PVP
    """
    racine.destroy()  # ferme le menu

    racine1 = tk.Tk()
    racine1.title("TAPANTA")
    canvas = tk.Canvas(racine1, bg="pale goldenrod", height=800, width=1000)
    canvas.grid(row=0, rowspan=5, column=0, columnspan=3)
    canvas.create_rectangle(100, 700, 700, 100, width=4, fill="pale goldenrod")

    # LIGNES
    canvas.create_line(100, 100, 700, 700, width=4, fill="black")
    canvas.create_line(100, 700, 700, 100, width=4, fill="black")
    canvas.create_line(400, 100, 400, 700, width=4, fill="black")
    canvas.create_line(100, 400, 700, 400,  width=4, fill="black")

    # ROND SUPERIEUR
    rond.append(canvas.create_oval(90, 90, 110, 110, fill="black"))
    rond.append(canvas.create_oval(390, 90, 410, 110, fill="black"))
    rond.append(canvas.create_oval(690, 90, 710, 110, fill="black"))

    # ROND MILLIEU
    rond.append(canvas.create_oval(90, 390, 110, 410, fill="black"))
    rond.append(canvas.create_oval(390, 390, 410, 410, fill="black"))
    rond.append(canvas.create_oval(690, 390, 710, 410, fill="black"))

    # ROND BAS
    rond.append(canvas.create_oval(90, 690, 110, 710, fill="black"))
    rond.append(canvas.create_oval(390, 690, 410, 710, fill="black"))
    rond.append(canvas.create_oval(690, 690, 710, 710, fill="black"))

    # LABEL SCORE
    label_J1 = tk.Label(racine1, bg="pale goldenrod",
                        text="Score Joueur 1 :" + "......")
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine1, bg="pale goldenrod",
                        text="Score Joueur 2 :" + "......")
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine1, bg="pale goldenrod",
                         command=None, text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine1, bg="pale goldenrod",
                         command=None, text="Charger")
    btn_LOAD.grid(row=2, column=2)
    btn_MENU = tk.Button(racine1, bg="pale goldenrod",
                         command=lambda: window_transition(1), text="Menu")
    btn_MENU.grid(row=3, column=2)

    # PROGRAMME :
    canvas.bind('<Button-1>', mouseover_item)

    racine1.mainloop()


def game_window_2():  # thibault
    global racine2
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*1000
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -4 boutons
        -Utilisé pour le IA V IA
    """
    racine.destroy()  # ferme le menu

    racine2 = tk.Tk()
    racine2.title("TAPANTA")
    canvas = tk.Canvas(racine2, bg="pale goldenrod", height=800, width=1000)
    canvas.grid(row=0, rowspan=5, column=0, columnspan=3)
    canvas.create_rectangle(100, 700, 700, 100, width=4, fill="pale goldenrod")

    # LIGNES
    canvas.create_line(100, 100, 700, 700, width=4, fill="black")
    canvas.create_line(100, 700, 700, 100, width=4, fill="black")
    canvas.create_line(400, 100, 400, 700, width=4, fill="black")
    canvas.create_line(100, 400, 700, 400,  width=4, fill="black")

    # ROND SUPERIEUR
    canvas.create_oval(90, 90, 110, 110, fill="black")
    canvas.create_oval(390, 90, 410, 110, fill="black")
    canvas.create_oval(690, 90, 710, 110, fill="black")

    # ROND MILLIEU
    canvas.create_oval(90, 390, 110, 410, fill="black")
    canvas.create_oval(390, 390, 410, 410, fill="black")
    canvas.create_oval(690, 390, 710, 410, fill="black")

    # ROND BAS
    canvas.create_oval(90, 690, 110, 710, fill="black")
    canvas.create_oval(390, 690, 410, 710, fill="black")
    canvas.create_oval(690, 690, 710, 710, fill="black")

    # LABEL SCORE
    label_J1 = tk.Label(racine2, bg="pale goldenrod",
                        text="Score Joueur :" + "......")
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine2, bg="pale goldenrod",
                        text="Score Ordinateur :" + "......")
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine2, bg="pale goldenrod",
                         command=None, text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine2, bg="pale goldenrod",
                         command=None, text="Charger")
    btn_LOAD.grid(row=2, column=2)
    btn_MENU = tk.Button(racine2, bg="pale goldenrod",
                         command=lambda: window_transition(2), text="Menu")
    btn_MENU.grid(row=3, column=2)
    btn_PAUSE = tk.Button(racine2, bg="pale goldenrod",
                          command=None, text="PAUSE")
    btn_PAUSE.grid(row=4, column=2)

    canvas.bind('<Button-1>', mouseover_item)

    racine2.mainloop()


def game_window_3():  # thibault
    global racine3
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*1000
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -4 boutons
        -Utilisé pour le IA V IA
    """
    racine.destroy()  # ferme le menu

    racine3 = tk.Tk()
    racine3.title("TAPANTA")
    canvas = tk.Canvas(racine3, bg="pale goldenrod", height=800, width=1000)
    canvas.grid(row=0, rowspan=5, column=0, columnspan=3)
    canvas.create_rectangle(100, 700, 700, 100, width=4, fill="pale goldenrod")

    # LIGNES
    canvas.create_line(100, 100, 700, 700, width=4, fill="black")
    canvas.create_line(100, 700, 700, 100, width=4, fill="black")
    canvas.create_line(400, 100, 400, 700, width=4, fill="black")
    canvas.create_line(100, 400, 700, 400,  width=4, fill="black")

    # ROND SUPERIEUR
    canvas.create_oval(90, 90, 110, 110, fill="black")
    canvas.create_oval(390, 90, 410, 110, fill="black")
    canvas.create_oval(690, 90, 710, 110, fill="black")

    # ROND MILLIEU
    canvas.create_oval(90, 390, 110, 410, fill="black")
    canvas.create_oval(390, 390, 410, 410, fill="black")
    canvas.create_oval(690, 390, 710, 410, fill="black")

    # ROND BAS
    canvas.create_oval(90, 690, 110, 710, fill="black")
    canvas.create_oval(390, 690, 410, 710, fill="black")
    canvas.create_oval(690, 690, 710, 710, fill="black")

    # LABEL SCORE
    label_J1 = tk.Label(racine3, bg="pale goldenrod",
                        text="Score Ordinateur 1 :" + "......")
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine3, bg="pale goldenrod",
                        text="Score Ordinateur 2 :" + "......")
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine3, bg="pale goldenrod", command=None,
                         text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine3, bg="pale goldenrod", command=None,
                         text="Charger")
    btn_LOAD.grid(row=2, column=2)
    btn_MENU = tk.Button(racine3, bg="pale goldenrod",
                         command=lambda: window_transition(3), text="Menu")
    btn_MENU.grid(row=3, column=2)
    btn_PAUSE = tk.Button(racine3, bg="pale goldenrod", command=None,
                          text="PAUSE")
    btn_PAUSE.grid(row=4, column=2)

    canvas.bind('<Button-1>', mouseover_item)

    racine2.mainloop()


def mouseover_item(event):  # jules
    ''' en fonction du clic du joueur retourne :
    - [x, y] si il sagit d'un point
    - [[x, y], [x, y]] si il sagit d'une ligne
    x, y sont des entiers correspondants aux positions
    des points dans MAP '''

    x, y = event.x, event.y

    # vérifications points (intersections)
    for elm in COORD_PTS:
        if (x > elm[0] and x < elm[2]) and (y > elm[1] and y < elm[3]):
            if JETONS[alterner_joueur()-1] > 0 and ETAT_PARTIE == 0:
                placer(elm[4])

    # vérification lignes
    for elm in COORD_LINES:
        if (x > elm[0] and x < elm[2]) and (y > elm[1] and y < elm[3]):
            if ETAT_PARTIE == 1:
                deplacer(elm[4])

    # vérifications diagonales
    for elm in COORD_DIAG:
        if (x > elm[0] and x < elm[2]) and (y > elm[1] and y < elm[3]):
            if x > (y-20) and x < (y+20):
                # diagonale d'équation x = size-y
                if ETAT_PARTIE == 1:
                    deplacer(elm[4])
            if x > (800-y-20) and x < (800-y+20):
                # diagonale d'équation x = y
                if ETAT_PARTIE == 1:
                    deplacer(elm[4])


def alterner_joueur():  # sophie
    ''' permet de savoir quel joueur joue,
    1 = tour rouge, 2 = tour bleu '''
    if TOUR_JEU % 2 == 0:
        return 1
    else:
        return 2


def alterner_tour():  # jules
    ''' alterne l'état de la partie pour savoir
    si on est en étape de placement / de déplacement '''
    global TOUR_JEU, ETAT_PARTIE
    if TOUR_JEU == 6:
        ETAT_PARTIE += 1


def placer(point):  # sophie
    ''' Poser les pions sur le plateau '''
    global TOUR_JEU, ETAT_PARTIE
    x, y = point[0], point[1]
    if MAP[x][y] == 0:
        MAP[x][y] = alterner_joueur()
        JETONS[alterner_joueur()-1] -= 1
        TOUR_JEU += 1
        alterner_tour()
        actualisation_graphique()


def deplacer(points):  # sophie
    ''' Déplacer les pions sur le plateau '''
    global pions_selectionner, TOUR_JEU, canvas, ETAT_PARTIE
    x1, y1 = points[0][0], points[0][1]
    x2, y2 = points[1][0], points[1][1]
    if (MAP[x1][y1] == 0 or MAP[x2][y2] == 0) and MAP[x1][y1] != MAP[x2][y2]:
        if max([MAP[x1][y1], MAP[x2][y2]]) == alterner_joueur():
            MAP[x1][y1], MAP[x2][y2] = MAP[x2][y2], MAP[x1][y1]
            TOUR_JEU += 1
            alterner_tour()
            actualisation_graphique()


def actualisation_graphique():  # sophie
    ''' Change en la couleur du joueur selon la MAP,
        si c'est des "1"(en rouge) ou des "2"(en bleu) '''
    global canvas
    for i in range(0, 3):
        for j in range(0, 3):
            if MAP[i][j] == 1:
                canvas.itemconfig(rond[i*3 + j], fill="red")
            elif MAP[i][j] == 2:
                canvas.itemconfig(rond[i*3 + j], fill="blue")
            else:
                canvas.itemconfig(rond[i*3 + j], fill="black")


menu()
