#연습문제 7 - 터틀 활용하여 다양한 칼라를 사용할 수 있는 방법을 살펴보고 다각형 그려보기 

import turtle as t 
t.shape('turtle')
a=['red','orange','yellow','violet','lightsalmon','green','blue']
for i in range(7):
    t.color(a[i])
    t.forward(100)
    t.right(360/7)


# 반복문을 활용하여 색상을 변경하며 trutle module로 도형 그려보기 
from turtle import*
shape('turtle')
pensize(5)
colormode(255)
goto(0,0)

col=255
col_t=0
for i in range(19,-1,-1):
    color(col,0,col_t)
    begin_fill()
    for j in range(i):
        forward(100)
        right(360/i)
    end_fill()
    col=col-int(255/19)
    col_t=col_t+int(255/19)