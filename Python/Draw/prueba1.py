from turtle import *

#la velocidad por defecto es tres
#speed('normal') #normal es 6 luego se aumenta
speed(2)
for i in range(4):
    fd(50)
    lt(80)

for i in range(8):
    undo()#deshace las instrucciones previamente ejecutadas

exitonclick()