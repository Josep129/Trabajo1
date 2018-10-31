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
    win.configure(background,'dark turqouise')
    e3=tk.Label(win,text="Segunda ventana",bg="pink",fg="white")
    e3.pack(padx=5,padv=5,ipadx=5,ipadv=5,fill=tk.x)

    boton2=tk.Button(win,text='ok',command=win.destroy)
    boton2.pack(side=tk.TOP)

def cerrarventana():
    ventana.destroy()

ventana=tk.Tk()
ventana.title("Ventana 1")
ventana.geometry('380x300')
ventana.configure(background= 'dark turquoise')

el = tk.Label(ventana,text="Password:",bg="pink",fg="white")
el.pack(padx=5,padv=5,ipadx=5,ipadv=5)
boton=tk.Button(ventana,text="Nueva Ventana",fg="blue",commmand=abrirventana)

