from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.messagebox import askyesno
from glob import glob
import re
import sqlite3

root = Tk()
root.title('Sql Tkinter App')
root.geometry("400x400")
root.iconbitmap('icon.ico')
root.config(bg="#6387AB")

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

#funzione delete item

def cancella():

    #creazione a datavbase
    conn = sqlite3.connect('indirizzi.db')

    #creazione del cursore
    c = conn.cursor() 

    #cancella record
    c.execute("DELETE from indirizzi WHERE oid=")
    #commit 
    conn.commit() 

    #chiudi connessione
    conn.close() 


#validazione campi input
def validation():
    nome = nome.get()
    msg = ''

    if len(nome) == 0:
        msg = ('il nome non può essere vuoto!')
    else:
        try:
            if any(ch.isdigit() for ch in nome):
                msg = ('il nome non può contenere numeri')
            elif len(nome) <= 2:
                msg = ('il nome non può essere di soli due caratteri')
            elif len(nome) > 100:
                msg = ('il nome non può avere piu di 99 caratteri')
            else:
                msg = ('successo')
        except Exception as ep:
            messagebox.showerror('message', ep)

#mostro Info
def showInfo():
    newWindow = Toplevel(root)
    newWindow.title("Finestra")
    newWindow.geometry("400x299")
    newWindow.config()

#accedo a finestra Views
def viewResult():
    root.destroy()
    import views

#check input fields 
def check_empty():
    if nome.entry(''):
       return True
    elif cognome.entry():
        return True
    elif indirizzo.entry():
        return True
    elif citta.entry():
        return True
    elif provincia.entry():
        return True
    elif zipcode.entry():
        return True
    else:
        print('campo richiesto')



#per gestire validazione email 
def show_message(error='', color='black'):
    label_error['text'] = error
    email_entry['foreground'] = color

def validate(value):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(pattern, value) is None:
        return False

    show_message()
    return True

# click event handler
def conferma():
    domanda = askyesno(title='conferma stato chiusura',
                    message='Sei sicuro di voler chiudere il programma ?')
    if domanda:
        root.destroy()

def chiudi():
    pass

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
nome.grid(row=0, column=1, padx=20, pady=(10, 0))

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
nome_label.grid(row=0, column=0, pady=(10, 0))

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

views_btn = Button(root, text="Risultati", command=viewResult)
views_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

close_btn = Button(root, text="Chiudi", command=conferma)
close_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

btn_info = Button(root, text="Info",command=showInfo)
btn_info.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#DELETE button
btn_delete = Button(root, text="Cnacella",command=cancella)
btn_delete.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#commit 
conn.commit() 

#chiudi connessione
conn.close() 

#lancio applicazione 
root.mainloop() 