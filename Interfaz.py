import tkinter as tk
from tkinter import messagebox

def validar():
    if entrada1.get()=='josep129':
        abrirventana2()
    else:
        messagebox.showwarning("Cuidado","Password Incorrecto")

def abrirventana2():
    ventana.withdrawn()
    win=tk.Toplevel()
    win.geometry('380x300+1900+100')
    win.configure(background='dark turqouise')
    e3=tk.Label(win,text="Segunda ventana",bg="pink",fg="white")
    e3.pack(padx=5,padv=5,ipadx=5,ipadv=5,fill=tk.X)

    boton2=tk.Button(win,text='ok',command=win.destroy)
    boton2.pack(side=tk.TOP)

def cerrarventana():
    ventana.destroy()

ventana=tk.Tk()
ventana.title("Ventana 1")
ventana.geometry('380x300')
ventana.configure(background= 'dark turquoise')

el = tk.Label(ventana,text="Password:",bg="pink",fg="white")
el.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
boton=tk.Button(ventana,text="Nueva Ventana",fg="blue",command=abrirventana2)
boton.pack(side=tk.TOP)
boton3=tk.Button(ventana,text="Validar Password",fg="blue",command=abrirventana2)
boton3.pack(side=tk.TOP)

ventana.mainloop()