###########################
# PROJET TAPATAN
# Jules Marty
# jihad Djiar
# Sophie Wu
# Adam Bouchaour
# Thibault Astier
###########################
# IMPORTS
import tkinter as tk
from tkinter import messagebox

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

POINTS_JOUEURS = [0, 0]  # joueur 1 / 2

MEMORY = []
REPETITION = []

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
    if id == 4:
        racine.destroy()
        game_window_1()
    if id == 5:
        racine.destroy()
        game_window_2()
    if id == 6:
        racine.destroy()
        game_window_3()
    if id == 11:
        racine1.destroy()
        game_window_1()


def menu():  # thibault
    global racine, POINTS_JOUEURS
    """ Fonction qui crée:
        -une fenetre de taille 400*400
        - 4 boutons: PvP, PvIA, IAvIA et Exit
        -Exit détruit la fenetre
    """
    POINTS_JOUEURS = [0, 0]
    racine = tk.Tk()
    racine.title("Menu")
    btn_PVP = tk.Button(racine, command=lambda: window_transition(4),
                        text="Player vs Player")
    btn_PVP.pack()
    btn_PVIA = tk.Button(racine, command=lambda: window_transition(5),
                         text="Player vs IA")
    btn_PVIA.pack()
    btn_IAVIA = tk.Button(racine, command=lambda: window_transition(6),
                          text="IA vs IA")
    btn_IAVIA.pack()
    btn_quit = tk.Button(racine, command=racine.destroy, text="Quitter")
    btn_quit.pack()
    racine.mainloop()


def game_window_1():  # thibault
    global racine1, canvas, racine
    """Fonction qui creer:
        -une nouvelle fenetre avec un canvas 800*800
        -avec le plateau (carre centré) 600*600
        -lignes et ronds au intersections
        -Utilisé pour le PVP
    """

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
                        text="Score Joueur 1 :" + str(POINTS_JOUEURS[0]))
    label_J1.grid(row=4, column=0)
    label_J2 = tk.Label(racine1, bg="pale goldenrod",
                        text="Score Joueur 2 :" + str(POINTS_JOUEURS[1]))
    label_J2.grid(row=4, column=1)

    # BOUTON
    btn_SAVE = tk.Button(racine1, bg="pale goldenrod",
                         command=sauvegarder, text="Sauvegarder")
    btn_SAVE.grid(row=1, column=2)
    btn_LOAD = tk.Button(racine1, bg="pale goldenrod",
                         command=charger, text="Charger")
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
        victory_check()


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
            victory_check()
            match_nul_check()


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


def affichage_messages(id):  # Jihad
    ''' gère l'ouverture et le contenu des fenetres d'informations
    présentés aux joueurs '''
    liste_message = ['match nul, personne ne gagne de point',
                     'point pour le joueur 1, bravo !',
                     'point pour le joueur 2, bravo !',
                     'le joueur 1 a gagné la partie !',
                     'le joueur 2 a gagné la partie !']
    messagebox.showinfo('information', liste_message[id])


def victory_check():  # Adam
    ''' vérifie si un des joueurs remporte le point '''
    win = 0
    # lignes
    for i in range(len(MAP)):
        if MAP[i][0] == MAP[i][1] == MAP[i][2] and MAP[i][0] != 0:
            win = MAP[i][0]
    # colonnes
    for i in range(len(MAP)):
        if MAP[0][i] == MAP[1][i] == MAP[2][i] and MAP[0][i] != 0:
            win += MAP[0][i]
    # diagonales
    if (MAP[0][0] == MAP[1][1] == MAP[2][2] and MAP[1][1] != 0) or\
            (MAP[2][0] == MAP[1][1] == MAP[0][2] and MAP[1][1] != 0):
        win += MAP[1][1]
    if win != 0:
        POINTS_JOUEURS[win-1] += 1
        affichage_messages(win)
        fin_de_partie()
        nouveau_tableau()


def nouveau_tableau():  # Adam
    ''' réinitialise le jeu et actualise le score '''
    global MAP
    global TOUR_JEU
    global ETAT_PARTIE
    global JETONS
    if 3 not in POINTS_JOUEURS:
        MAP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        TOUR_JEU = 0
        ETAT_PARTIE = 0
        JETONS = [3, 3]
        window_transition(11)


def match_nul_check():  # Adam
    ''' vérifie si le même tableau apparait 3 fois a partir du
    moment ou les joueurs déplaces leurs jetons '''
    if str(MAP) in MEMORY:
        REPETITION[MEMORY.index(str(MAP))] += 1
    else:
        MEMORY.append(str(MAP))
        REPETITION.append(1)
    if 3 in REPETITION:
        affichage_messages(0)
        nouveau_tableau()


def fin_de_partie():  # jihad
    ''' met fin a la partie si un joueur atteint 3 point '''
    if POINTS_JOUEURS[0] == 3:
        affichage_messages(3)
        window_transition(1)
    if POINTS_JOUEURS[1] == 3:
        affichage_messages(4)
        window_transition(1)


def sauvegarder():  # jihad
    ''' sauvegarde la partie en cours '''
    fichier_sauvegarde = open('save', 'w')
    temp = ''
    for elm in MAP:
        for s_elm in elm:
            temp += str(s_elm)
    temp += '|'
    temp += str(POINTS_JOUEURS[0]) + str(POINTS_JOUEURS[1])
    temp += '|'
    temp += str(JETONS[0]) + str(JETONS[1])
    temp += '|'
    temp += str(TOUR_JEU)
    temp += '|'
    temp += str(ETAT_PARTIE)
    fichier_sauvegarde.write(temp)


def charger():  # jules
    ''' charge la dernière partie sauvegardé '''
    global MAP, POINTS_JOUEURS, JETONS, TOUR_JEU, ETAT_PARTIE
    fichier = open('save', 'r')
    chaine = fichier.read()
    liste = []
    temp = []
    for elm in chaine:
        if elm != '|':
            temp.append(elm)
        else:
            liste.append(temp)
            temp = []
    liste.append(temp)
    print(liste)
    MAP = [[int(liste[0][0]), int(liste[0][1]), int(liste[0][2])],
           [int(liste[0][3]), int(liste[0][4]), int(liste[0][5])],
           [int(liste[0][6]), int(liste[0][7]), int(liste[0][8])]]
    POINTS_JOUEURS = [int(liste[1][0]), int(liste[1][1])]
    JETONS = [int(liste[2][0]), int(liste[2][1])]
    TOUR_JEU = int(liste[3][0])
    ETAT_PARTIE = int(liste[4][0])
    actualisation_graphique()


menu()
