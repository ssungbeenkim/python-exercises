import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color('brown','yellow')# 선색, 채우는색(거북이 채워짐) 

def opening():
    print('게임의 룰을 설명')

def drawPol(n):
    for i in range(n):
        t.forward(100)
        t.right(360/n)

def right(n):
    for i in range(n):
        t.forward(100)
        t.right(360/n)

def left(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n)

right(5)


