from turtle import *


speed(1)
penup()#no dibuja solo mueve la tortuga
fd(80)
pendown()#dibuja
right(45)
fd(82)
pensize(20)#cambia el tamaño de la linea
fd(42)
#podemos cambiar la configuracion de la tortuga
pen(fillcolor="black",pencolor="green",pensize=10)
#fillcolor color de la tortuga
#pencolor color de la linea
#pensize grosor de la linea
for i in range(4):
    fd(40)
    right(90)
right(45)
fd(56)
pen(shown=False,speed=1,outline=12)
for i in range(4):
    fd(40)
    right(90)

exitonclick()