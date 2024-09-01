from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)#no se puede cambiar el tamaño si es 0,0
#si es uno en alguno se se puede en ese eje
raiz.iconbitmap('image/book.ico')
raiz.geometry("650x350")
raiz.config(bg="lightblue")
raiz.mainloop()