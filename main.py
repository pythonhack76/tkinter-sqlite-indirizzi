from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Sql Tkinter App')
root.geometry("400x400")

#Database

#creazione a datavbase
conn = sqlite3.connect('indirizzi.db')

#creazione del cursore
c = conn.cursor() 

#creeazione della tabella
'''
c.execute("""CREATE TABLE indirizzi (
    nome text,
    cognome text,
    indirizzo text,
    citta text,
    provincia text,
    zipcode integer
    )""") 
'''
##### WIDGET text boxes #######
nome = Entry(root, width=30)
nome.grid(row=0, column=1, padx=20)

cognome = Entry(root, width=30)
cognome.grid(row=1, column=1, padx=20)

indirizzo = Entry(root, width=30)
indirizzo.grid(row=2, column=1, padx=20)

citta = Entry(root, width=30)
citta.grid(row=3, column=1, padx=20)

provincia = Entry(root, width=30)
provincia.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

##### WIDGET label boxes #######

nome_label = Label(root, text="Nome")
nome_label.grid(row=0, column=0)

cognome_label = Label(root, text="Cognome")
cognome_label.grid(row=1, column=0)

indirizzo_label = Label(root, text="indirizzo")
indirizzo_label.grid(row=2, column=0)

citta_label = Label(root, text="citta")
citta_label.grid(row=3, column=0)

provincia_label = Label(root, text="provincia")
provincia_label.grid(row=4, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)
#commit 
conn.commit() 

#chiudi connessione
conn.close() 

#lancio applicazione 
root.mainloop() 