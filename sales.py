from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.messagebox import askyesno
from glob import glob
import re
import sqlite3

root = Tk()
root.title('SALES App')
root.geometry("400x400")
root.iconbitmap('icon.ico')
root.config(bg="#6387AB")

#Database

#creazione a datavbase
conn = sqlite3.connect('sales.db')

#creazione del cursore
c = conn.cursor() 

#creeazione della tabella
'''
c.execute("""CREATE TABLE acquisti (
    fornitore text,
    fattura text,
    data text,
    importo integer,
    pagamento text,
    pagato text
    )""") 
'''

##### values OF program #####

var = StringVar(value="testo della label")

##### WIDGET Funzioni #######

#funzione delete item

def cancella():

    #creazione a datavbase
    conn = sqlite3.connect('sales.db')

    #creazione del cursore
    c = conn.cursor() 

    #cancella record
    c.execute("DELETE from acquisti WHERE oid=")
    #commit 
    conn.commit() 

    #chiudi connessione
    conn.close() 


#validazione campi input
def validation():
    fornitore = fornitore.get()
    msg = ''

    if len(nome) == 0:
        msg = ('il fornitore non può essere vuoto!')
    else:
        try:
            if any(ch.isdigit() for ch in fornitore):
                msg = ('il nome non può contenere numeri')
            elif len(fornitore) <= 2:
                msg = ('il nome non può essere di soli due caratteri')
            elif len(fornitore) > 100:
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
    if fornitore.entry(''):
       return True
    elif fattura.entry():
        return True
    elif data.entry():
        return True
    elif importo.entry():
        return True
    elif pagamento.entry():
        return True
    elif pagato.entry():
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
    conn = sqlite3.connect('sales.db')

    #creazione del cursore
    c = conn.cursor() 

  

    #inserisci nella tabella
    c.execute("INSERT INTO acquisti VALUES (:fornitore, :fattura, :data, :importo, :pagamento, :pagato)",
            {
                'fornitore': fornitore.get(),
                'fattura': fattura.get(),
                'data': data.get(),
                'importo': importo.get(),
                'pagamento': pagamento.get(),
                'pagato': pagato.get(),

            }   

    
    
    
        )

    #commit 
    conn.commit() 

    #chiudi connessione
    conn.close() 


    #pulisci il text boxes
    fornitore.delete(0, END)
    fattura.delete(0, END)
    data.delete(0, END)
    importo.delete(0, END)
    pagamento.delete(0, END)
    pagato.delete(0, END)
    




##### WIDGET text boxes #######
fornitore = Entry(root, width=30)
fornitore.grid(row=0, column=1, padx=20, pady=(10, 0))

fattura = Entry(root, width=30)
fattura.grid(row=1, column=1, padx=20)

data = Entry(root, width=30)
data.grid(row=2, column=1, padx=20)

importo = Entry(root, width=30)
importo.grid(row=3, column=1, padx=20)

pagamento = Entry(root, width=30)
pagamento.grid(row=4, column=1, padx=20)

pagato = Entry(root, width=30)
pagato.grid(row=5, column=1, padx=20)

##### WIDGET label boxes #######

fornitore_label = Label(root, text="Fornitore", bg="#6387AB")
fornitore_label.grid(row=0, column=0, pady=(10, 0))

fattura_label = Label(root, text="Fattura", bg="#6387AB")
fattura_label.grid(row=1, column=0)

data_label = Label(root, text="Data", bg="#6387AB")
data_label.grid(row=2, column=0)

importo_label = Label(root, text="importo", bg="#6387AB")
importo_label.grid(row=3, column=0)

#provincia_label = Label(root, text="provincia", bg="#6387AB")
pagamento_label = Label(root, text="pagamento", bg="#6387AB")
pagamento_label.grid(row=4, column=0)

pagato_label = Label(root, text="pagato", bg="#6387AB")
pagato_label.grid(row=5, column=0)


##### WIDGET bottoni #######

#Inserisci Record
submit_btn = Button(root, text="Aggiungi", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Visualizza Record
views_btn = Button(root, text="Risultati", command=viewResult)
views_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Chiudi Finestra e Programma
close_btn = Button(root, text="Chiudi", command=conferma)
close_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Mostra Info
btn_info = Button(root, text="Info",command=showInfo)
btn_info.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#DELETE button
btn_delete = Button(root, text="Cacella",command=cancella)
btn_delete.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#commit 
conn.commit() 

#chiudi connessione
conn.close() 

#lancio applicazione 
root.mainloop() 