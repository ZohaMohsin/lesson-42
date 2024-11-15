import turtle
turtle.Screen().bgcolor("black")
sc=turtle.Screen()
turtle.title("square")
colors={'red', 'green', 'blue', 'yellow' ,'purple' ,'orange'}
t1=turtle.Turtle()
t1.speed('fastest')
t1.hideturtle()
while True:
    for x in range(200):
        t1.pencolor(colors[x%len(colors)])
        t1.width(x/100 + 1)
        t1.forward(x)
        t1.left(59)
    t1.right(239)
    for x in range(200, 0 ,-1):
        t1.pencolor('balck')
        t1.width(x/100 + 1)
        t1.forward(x)
        t1.right(59)
        
turtle.done()


