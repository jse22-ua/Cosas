from turtle import *
from tkinter import *

""" muñeco de nieve
dot(50,"lightblue") #dibuja circulos de ese radio y ese color
sety(-74)
dot(100,"lightblue")
"""

root = Tk() 
color("blue")
astamp=stamp()#hace una copia
fd(50)
clearstamp(astamp)#elimina la copia

for i in range(8):
    stamp(); fd(30)

"""title("Gui Button")


btn1 = Button(root,text="botton",command=lambda:clearscreen())

for i in range(5):
    btn1.pack()"""

circle(50)

mainloop()