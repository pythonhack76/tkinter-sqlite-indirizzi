from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('3view')
ws.geometry('400x300')
ws['bg']='#fb0'

tv = ttk.Treeview(ws)
tv['columns']=('nome', 'cognome', 'indirizzo')
tv.column('#0', width=0, stretch=NO)
tv.column('nome', anchor=CENTER, width=80)
tv.column('cognome', anchor=CENTER, width=80)
tv.column('indirizzo', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('nome', text='Nome', anchor=CENTER)
tv.heading('cognome', text='cognome', anchor=CENTER)
tv.heading('indirizzo', text='indirizzo', anchor=CENTER)

tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
tv.pack()


ws.mainloop()