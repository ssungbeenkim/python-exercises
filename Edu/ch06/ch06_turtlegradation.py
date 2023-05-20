from turtle import *
shape('turtle')
pensize(10)
colormode(255) #0~255
goto(0,100)

col=255
col_t=0
for i in range(19,-1,-1):
    color(0,col,col_t)
    begin_fill()
    for j in range(i):
        forward(100)
        right(360/i)
    end_fill()
    col=col-int(255/19)
    col_t=col_t+int(255/19)