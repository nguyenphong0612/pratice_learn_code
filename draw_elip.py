import turtle as t
elip = t.Turtle()
color = ["red", "green", "blue", "light green", "grey", "yellow", "black", "brown"]

for j in range(61):
    for i in range(2):
        elip.speed(10)
        elip.pencolor(color[j%8])
        elip.circle(100, 90)
        elip.circle(50, 90)
    elip.rt(5)


t.done()
