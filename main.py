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

##### WIDGET Funzioni #######

def submit():

    #creazione a datavbase
    conn = sqlite3.connect('indirizzi.db')

    #creazione del cursore
    c = conn.cursor() 

    #inserisci nella tabella
    c.execute("INSERT INTO indirizzi VALUES (:nome, :cognome, :indirizzo, :citta, :provincia, :zipcode)",
            {
                'nome': nome.get(),
                'cognome': cognome.get(),
                'indirizzo': indirizzo.get(),
                'citta': citta.get(),
                'provincia': provincia.get(),
                'zipcode': zipcode.get(),

            }   

    
    
    
        )

    #commit 
    conn.commit() 

    #chiudi connessione
    conn.close() 


    #pulisci il text boxes
    nome.delete(0, END)
    cognome.delete(0, END)
    indirizzo.delete(0, END)
    citta.delete(0, END)
    provincia.delete(0, END)
    zipcode.delete(0, END)
    




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


##### WIDGET bottoni #######

submit_btn = Button(root, text="Aggiungi", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#commit 
conn.commit() 

#chiudi connessione
conn.close() 

#lancio applicazione 
root.mainloop() 