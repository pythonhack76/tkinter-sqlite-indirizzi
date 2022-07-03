import tkinter as tk
root = tk.Tk() 
root.geometry("650x450")
root.title("App Entry Box")

numero_di_campi = 5
ref= []

for j in range(numero_di_campi):
    l=tk.Label(root, text='Inserisci' + str(j+1), font=20, fg='blue')
    l.grid(row=j, column=0, padx=10)

    e=tk.Entry(root, text=j, font=20, bg='lightyellow')
    e.grid(row=j, column=1, padx=10, pady=10)

    ref.append(e)



root.mainloop() 