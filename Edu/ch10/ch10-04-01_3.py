from turtle import*
shape('turtle')
pensize(5)
# 반복문을 활용하여 색상을 변경하며 trutle module로 도형 그려보기 
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