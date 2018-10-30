from tkinter import *

def validar():
    if entrada1.get()=="josep129":
        abrirventana()
    else:
        messagebox.showwarning("Cuidado","Password Incorrecto")

def abrirventana():
    ventana.withdrawn()
    win=tk.Toplevel()
    win.geometry()
    win.configure(background,"dark turqouise")
    e3=tk.Label(win,text="Segunda ventana",bg="pink",fg="white")
    e3.pack(padx=5,padv=5)