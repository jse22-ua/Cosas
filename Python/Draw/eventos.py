from turtle import *

def turn(x,y):
    left(180)
"""
onclick(turn)#crea el evento que ocurre cuando pulsas la tortuga
onclick(None)#elimina el evento
screen = Screen()
screen.onclick(turn)#evento cuando pulsas la pantalla
"""

class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")

turtle = MyTurtle()
turtle.onclick(turtle.glow)
turtle.onrelease(turtle.unglow)

ondrag(goto)#cuando arrastas



mainloop()