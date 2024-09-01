from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)#no se puede cambiar el tamaño si es 0,0
#si es uno en alguno se se puede en ese eje
raiz.iconbitmap('image/book.ico')
raiz.config(bg="lightblue")
raiz.config(cursor="hand2")
miFrame = Frame()#marco
miFrame.pack(side="bottom",anchor="w",fill="x")#se queda anclado en abajo
miFrame.config(bg='red')
miFrame.config(width="650",height='350')
miFrame.config(bd=35)#grosor del borde del frame
miFrame.config(relief="groove")#tipo de borde
miFrame.config(cursor="pirate")#tipo de cursor
raiz.mainloop()