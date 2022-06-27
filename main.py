from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Sql Tkinter App')
root.geometry("400x400")

#Database

#creazione a datavbase
conn = sqlite3.connect('indirizzi.db')



#lancio applicazione 
root.mainloop() 