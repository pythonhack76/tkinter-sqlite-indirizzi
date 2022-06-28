from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import askyesno
from glob import glob
import re
import sqlite3

root = Tk()
root.title('Sql Tkinter App')
root.geometry("400x400")

#Database

#creazione a datavbase
conn = sqlite3.connect('indirizzi.db')

#creazione del cursore
c = conn.cursor() 

##### FUNCTIONS ##################

def query():
    #creazione a datavbase
    conn = sqlite3.connect('indirizzi.db')

    #creazione del cursore
    c = conn.cursor() 

    #eseguo
    c.execute("SELECT *, oid FROM indirizzi ")
    records = c.fetchall()
    print(records)

    #commit 
    conn.commit() 

    #chiudi connessione
    conn.close() 



##### WIDGET bottoni #######

query_btn = Button(root, text="Mostra Records", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)






#commit 
conn.commit() 

#chiudi connessione
conn.close() 

#lancio applicazione 
root.mainloop() 