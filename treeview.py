from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()
root.title('treeview')
root.iconbitmap('icon.ico')
root.geometry("1000x500")


#connessione al database
conn = sqlite3.connect('indirizzi.db')

c = conn.cursor() 

c.execute("SELECT * FROM indirizzi")
records = c.fetchall()

#aggiungi i dati in video
global count 
count = 0 

for record in records:
    print(record)

for record in records: 
    if count % 2 == 0:
        my_tree.insert(parent='', index='end')
    else:
        my_tree.insert(parent='', index='end')
    #incremento contatore
    count += 1

conn.commit()

conn.close()

def query_database():
    #creazione db
    conn = sqlite3.connect('indirizzi.db')

    c = conn.cursor() 




query_database() 


root.mainloop() 