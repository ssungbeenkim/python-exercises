import turtle as tt
s = tt.Screen()
t1 = tt.Turtle()
t1.shape('turtle')
t1.color('blue', 'yellow')
t1.width(2)
cc = ['red', 'green', 'blue', 'yellow', 'purple']
for i in range(9):
    t1.color(cc[i % 5])
    t1.fd(100)
    t1.rt(90)
    t1.circle(20)
    t1.lt(90)
    t1.bk(100)
    t1.lt(40)
