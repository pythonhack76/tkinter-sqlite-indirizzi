import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime

root = tk.Tk()
root.title("Titolo Data Picker")
root.geometry("400x200")

def my_upd(*args):
    cal_label.config(text=sel.get())

sel= tk.StringVar()
cal=DateEntry(root, selectmode='day', textvariable=sel )
cal.grid(row=1, column=1, padx=20, pady=30)


cal_label = Label(root, bg='yellow')
cal_label.grid(row=2, column=0, padx=20, pady=20)

sel.trace('w', my_upd)

root.mainloop()


