from pygame import *
import sys

init()
pantalla = display.set_mode((500,400))#500 ancho; 400 largo
display.set_caption('Mi primer juego :D')#titulo
pantalla.fill("#5dc1b9")#coger ese color

#dibujar figuras
'''draw.rect(pantalla, "#F80044",(100,50,100,50))#rectangulo rojo de 100x50
draw.line(pantalla, "#2d572c",(100,104),(199,104),1)
#dibuja una linea verde (100,104) punto inicio
#(199,104) punto final; 1 grosor de la linea
draw.circle(pantalla,"#FFFFFF",(122,250),20,0)
#(122,250) posicion del centro; 20 radio;0 para decir que esta vacio
draw.ellipse(pantalla,"#61cd35",(275,200,40,80),10)
#dibuja una elipse dos primeros numeros posicion
#dos siguientes el tamaño si fuera un rombo 
#40 seria lo que mediria la diagonal del eje x y el 80 la diagonal de y
puntos = [(200,100),(300,50),(400,200),(350,200),(250,400)]
draw.polygon(pantalla,(12,150,255),puntos,5)
#dibuja un poligono de cinco lados irregular'''
#poner imagenes
fondo=image.load("image/fondo.png")
icono = image.load("image/icono.png")
pantalla.blit(fondo,(0,0))
display.set_icon(icono)

while True:

    for evento in event.get():
        if evento.type == QUIT:
            quit()
            sys.exit()
    display.update()#le pone color al fondo que hemos puesto a fill
