
import random 
import turtle
t = turtle.Turtle()
t.shape('turtle')

def left():
    t.left(30)
    t.forward(10)

def forwd():
    t.forward(10)

def backwd():
    t.back(10) 

def right():
    t.right(30)
    t.forward(10)

screen=t.getscreen() # Important

screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
screen.onkeypress(forwd,"Up")
screen.onkeypress(backwd,"Down")

screen.listen() # key 입력모드를 실행하도록 해준다. 


