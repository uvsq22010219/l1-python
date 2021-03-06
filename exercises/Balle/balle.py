import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
nb_rebonds = 0

###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global rayon
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    if nb_rebonds < 30:
        rebond()
        changercouleur()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, nb_rebonds
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x1 <= 0 or x1 >= 600:
        nb_rebonds +=1
        balle[1] = -balle[1]
    
    if y0 <= 0 or y0 >= 400:
        nb_rebonds +=1
        balle[2] = -balle[2]    

def changercouleur():
    """Fait changer la balle de la couleur de la zone dans laquelle elle se trouve"""
    global balle, rayon
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if y1 <= 50:
        if 0 <= x0 < (150 - rayon):
            canvas.itemconfig(balle[0], fill="red")
        elif 150 <= x0 < (300 - rayon):
            canvas.itemconfig(balle[0], fill="green")
        elif 300 <= x0 < (450 - rayon):
            canvas.itemconfig(balle[0], fill="blue")
        elif 450 <= x0 <= (600 - rayon):
            canvas.itemconfig(balle[0], fill="yellow")

        

######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
zone1 = canvas.create_rectangle((0,0), (150,50), fill="red")
zone2 = canvas.create_rectangle((150,0), (300,50), fill="green")
zone3 = canvas.create_rectangle((300,0), (450,50), fill="blue")
zone4 = canvas.create_rectangle((450,0), (600,50), fill="yellow")
balle = creer_balle()
mouvement()
racine.mainloop()
