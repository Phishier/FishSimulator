import turtle
import time
import random
import math

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

wn = turtle.Screen()
wn.bgcolor("lightblue")


speed = 1

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed 
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

wn.listen()
wn.onkey(turnleft, "Left")
wn.onkey(turnright, "Right")
wn.onkey(increasespeed, "Up")
wn.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)
