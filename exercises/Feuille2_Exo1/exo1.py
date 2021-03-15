import tkinter as tk
import random as rd

etat_balle = 1

root = tk.Tk()

def creer_balle():
    """Créer une balle"""
    circle = c.create_oval((300-20, 200-20), (300+20, 200+20), fill="blue")
    x = rd.randint(1,7)
    y = rd.randint(1,7)
    return [circle, x, y]

def mouvement(b):
   """Mouvoir la balle dans une direction aléatoire selon les valeurs de la liste balle"""
   global id_after
   c.move(b[0], b[1], b[2])
   rebond2(b)
   id_after = c.after(30, lambda: mouvement(b))

def start():
    """Démarrer le mouvement de la balle"""
    global etat_balle
    if etat_balle == 1 : 
        mouvement(balle)
        button.config(text="Arrêter")
    else :
        c.after_cancel(id_after)
        button.config(text="Démarrer")
    etat_balle = 1 - etat_balle

def rebond1(balle):
    x0, y0, x1, y1 = c.coords(balle[0])
    if y1 >= 400 or y0 <= 0 :
        balle[2] = -balle[2]
    if x1 >= 600 or x0 <= 0 :
        balle[1] = -balle[1]

def rebond2(b):
    x0, y0, x1, y1 = c.coords(b[0])
    if y1 >= 400:
        c.coords(b[0], x0, 0, x1, y0+40)
    if x1 >= 600:
        c.coords(b[0], 0, y0, x0+40, y1)


c = tk.Canvas(root, height=400, width=600, bg="black")
button = tk.Button(root, text="Démarrer", font="20", command=start)
balle = creer_balle()

c.grid(row=0)
button.grid(row=1)

root.mainloop()
