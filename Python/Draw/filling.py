from turtle import *

begin_fill()
if filling():
    pensize(52)
else:
    pensize(3)

fd(52)

color("black","red")
begin_fill()# empieza a rellenar 
circle(80)
end_fill()#deja de rellenar

right(90)
pensize(20)
fd(10)
color("green","aqua")#el color de la tortuga determina de que color será la tortuga
begin_fill()
for i in range(4):
    fd(100)
    right(90)
end_fill()

exitonclick()