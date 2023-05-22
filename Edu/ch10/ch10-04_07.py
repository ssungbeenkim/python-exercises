import turtle as t 
t.shape('turtle')
a=['red','orange','yellow','violet','lightsalmon','green','blue']
for i in range(7):
    t.color(a[i])
    t.forward(100)
    t.right(360/7)