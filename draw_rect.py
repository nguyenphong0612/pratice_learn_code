import turtle as t
rect = t.Turtle()
rect.hideturtle()
rect.penup()
rect.goto(-50, 25)
rect.pencolor("blue")
rect.pensize(3)
rect.fillcolor("red")
rect.begin_fill()
rect.pendown()
for i in range(2):
    rect.fd(100)
    rect.rt(90)
    rect.fd(50)
    rect.rt(90)

rect.end_fill()
t.done()