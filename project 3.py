import turtle

t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(200, 0)
t.pendown()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-200, 0)
t.pendown()

for i in range(6):
    t.forward(80)
    t.left(60)

turtle.done()










