print("                       Discord : >Lirox’s#1337")
print("                       By : >Lirox’s#1337     ")

print("")
print("")

print("                                RAPPEL ET REGLE DU JEU")
print("")
print("1° Vous ne pouvez que rentrer des nombres de 0 à 1000.")
print("")
print('2° Tant que le jeu n’est pas fini vous devez "entrer un prix".')
print("")
print("3° Le jeu vous annonce si votre nombre est inférieur et/ou supérieur.")
print("")
print("4° Si vous trouvez la réponse le jeu vous annonceras votre Win.")
print("")
print("5° Le jeu s'arretera au bout de 120 secondes automatiquement.")
print("")
print("6° Vous avez également 25 tentatives.")
print("")
print(                          "BONNE CHANCE A VOUS !")
print("")

reglement = input("A present pouvez vous acceptez les règles avant de jouer ? (oui, non):")
if reglement == "oui":
     running = True	

print("")
jouer = input("Bonjour vous y etes donc voici le jeu du juste prix voulez vous jouez à ce jeu ? (oui, non) :")
if jouer == "oui":
	running = True
else:
	running = False

from email.mime import image
from errno import ENETRESET
from pickle import FRAME
import random


import time


import tkinter as tk
from tkinter.filedialog import askopenfilename



def essai(event=None):

    global entree_proposition, nombre_hasard, tentatives, tentativestxtvar, infovar

    
    proposition = entree_proposition.get()

    
    if proposition.isdigit():
       
        nombre_proposition = int(proposition)

        
        if nombre_proposition < nombre_hasard:
            infovar.set("Merci de rentrer un nombre supérieur.")
        elif nombre_proposition > nombre_hasard:
            infovar.set("Merci de donner un nombre inférieur.")
        else:
            infovar.set("C'est win ! Merci d'avoir jouer.")
            

        tentatives -= 1 
        tentativestxtvar.set(f"{tentatives} tentatives")

    else:
        infovar.set("Tu dois entrer un nombre")



tentatives = 25


temps = time.time()

color = "#8A2BE2"


nombre_hasard = random.randint(1, 1000)


fenetre = tk.Tk()
fenetre.geometry("600x300")
fenetre.title("Jeu du juste prix by Lirox's")
fenetre.resizable(width=False, height=False)
fenetre.config(bg=color)

frame = tk.Frame(fenetre)
frame.pack(expand=True)

entree_proposition = tk.Entry(frame)
entree_proposition.bind('<Return>', essai)
entree_proposition.focus()
entree_proposition.pack()


bouton = tk.Button(frame, text="Valider", command=essai)
bouton.pack()

#Les Alertes
from tkinter.messagebox import *
def callback():
    if askyesno("Mal ou bien ?", 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning("Dommage c'est 10 sec de perdu", 'Tant pis...')
        time.sleep(10)
        info.place(x=200, y=50)
        
       


    else:
        showinfo('Ouf', 'Vous avez peur!')
        showerror("", "Ahah")


tk.Button(text='Action', command=callback).pack()

infovar = tk.StringVar()
infovar.set("Jeux By Lirox's")
info = tk.Label(fenetre, textvariable=infovar, bg=color)
info.place(x=265, y=220)



infovar = tk.StringVar()
infovar.set("Discord : >Lirox’s#1337")
info = tk.Label(fenetre, textvariable=infovar, bg=color)
info.place(x=220, y=50)

tentativestxtvar = tk.StringVar()
tentativestxtvar.set("25 tentatives")

tentativestxt = tk.Label(fenetre, textvariable=tentativestxtvar, bg=color)
tentativestxt.place(x=500, y=20)


tempsvar = tk.StringVar()
tempsvar.set("120")
tentativestxt = tk.Label(fenetre, textvariable=tempsvar, bg=color)
tentativestxt.place(x=20, y=20)


fenetre.mainloop()
