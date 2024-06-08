from datetime import datetime
import turtle as t
import random as r
screen = t.Screen()
screen.setup(600, 600)
screen.title("Race run of Turtles")
screen.bgcolor("light green")
turtle_gr = []

p = t.Turtle()
colors = ("black", "red", "blue", "green", "yellow")
p.hideturtle()
p.rt(90)
p.penup()

for i in range(5):
    x = -250
    y_pos = i*70-140
    turtles = t.Turtle(shape="turtle")
    turtles.color(colors[i])
    turtles.penup()
    turtles.goto(x=-250, y=y_pos)
       
    for k in range(6):
        turtles.rt(60)
    turtle_gr.append(turtles)
for j in range(11):
    p.goto(-250+j*50, 205)
    p.write(j)
    for i in range(5):
        p.penup()
        p.fd(60)
        p.pendown()
        p.fd(10)
        p.penup()
    p.fd(70)    
    p.write(j)   

    """for k in range(11):
        # tạo sọc kẻ đường đi của rùa
        
        cross.hideturtle()
        cross.penup()
        cross.goto(-250, 140)
        cross.goto(x=-250+k*50, y= 5+y_pos) # vị trí mỗi kẻ sọc (+5) theo trục ngang với rùa, cách nhau 50
        cross.pendown()
        cross.rt((1+(-i)//4)*(1+(-k)//10)*90)# chỉ trường hợp i, k = 0 thì quay 90, còn lại giữ nguyên hướng
        cross.fd(10) # kẻ sọc với độ lớn 10
        p.penup()
        # Ghi số 2 bên lề đường chạy
        p.hideturtle()
        
        p.goto(x=-250+k*50, y= ((i//4)*280-140)-(1-2*(i//4))*20) # chỉ khi i = 0, 4 mới ghi, khi thấp hơ, khi cao hơn sọc kẻ đường
        p.write(k) # ghi chỉ số vạch đường
    # Tạo tốc độ ban đầu"""
    
# Tạo hàm chạy đua   
def race_run(turtles):
    global run
    for i in range(len(turtles)):
        turtles[i].fd(5*r.randint(1,5))
        if turtles[i].xcor() >= 250:
            t.hideturtle()
            t.penup()
            t.goto(0,200)
            t.pendown()
            t.write(f"turtle {i} with color {colors[i]} win ")
            run = False
run = True
while run:     
    
    time = datetime.now()
    t.write(time.second)
    race_run(turtle_gr)
    
screen.exitonclick()
#t.done()