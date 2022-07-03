from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    conn = sqlite3.connect("indirizzi.db")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    conn.commit()
    conn.close()

def insert():
    conn = sqlite3.connect("indirizzi_web.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    conn.commit()
    conn.close()



def View():
    conn = sqlite3.connect("indirizzi.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM indirizzi")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

root = tk.Tk()
root.geometry("1000x400")

tree= ttk.Treeview(root, column=("column1", "column2", "column3","column4","column5","column6"), show='headings')
tree.heading("#1", text="NOME")
tree.heading("#2", text="COGNOME")
tree.heading("#3", text="INDIRIZZO")
tree.heading("#4", text="CITTA")
tree.heading("#5", text="PROVINCIA")
tree.heading("#6", text="ZIPCODE")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()