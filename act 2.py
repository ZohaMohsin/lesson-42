import turtle
turtle.Screen().bgcolor("green")
sc=turtle.Screen()
sc.setup(400,300)

turtle.title("triangle")

t1=turtle.Turtle()
for i in range(3):
    t1.forward(100)
    t1.left(120)
    i=i+1



t1.penup()
t1.right(-90)
t1.forward(50)

t1.pendown()
t1.right(90)
for i in range(3):
    t1.forward(100)
    t1.right(120)
    i=i+1

turtle.done()


