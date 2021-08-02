'''
Proyecto: Videojuego carrera de tortugas con Interfaz Gráfica en Turtle
Elaborado por: Karina Flores G. y Gabriel Alejandro Herrera G. 
Fecha: 28 julio 2021
'''
#Importamos bibliotecas necesarias para la creación del juego
#Turtle para la interfaz gráfica y Random para la obtención de npumeros aleatorios
from turtle import Turtle
from turtle import Screen
import random

#Variables de control para el juego
carrera = False
pantalla = Screen()
pantalla.setup(width=500, height=400)
pantalla.bgcolor("#94FF33")
tortuga_elegida = pantalla.textinput(title="Haz tu apuesta !! ", prompt="Con qué tortuga quieres competir? Elige un color: ")
tortugas = []

colores = ["red", "orange", "yellow", "green", "blue", "purple"]

for tortuga_index in range(6):
  nueva_tortuga = Turtle(shape="turtle")
  nueva_tortuga.color(colores[tortuga_index])
  nueva_tortuga.penup()
  nueva_tortuga.goto(x=-230, y=-75 + tortuga_index * 30)

  tortugas.append(nueva_tortuga)


if tortuga_elegida:
  carrera = True

while carrera:
  for tortuga in tortugas:
    random_distance = random.randint(0, 10)
    tortuga.forward(random_distance)

    if tortuga.xcor() > 230:
      carrera = False
      ganador = tortuga.pencolor()

      if ganador == tortuga_elegida:
        print(f"GANASTE! La tortuga  {ganador} es la vencedora!")
      else:
        print(f"PERDISTE! La tortuga  {ganador} es la vencedora!")

    
      

pantalla.exitonclick()