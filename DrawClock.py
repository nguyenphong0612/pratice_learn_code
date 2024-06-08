import turtle as t
from random import randint
from datetime import datetime, time
# Khởi tạo màn hình
screen = t.Screen()
screen.setup(500, 500)
screen.bgcolor("light green")
screen.title("CLOCK")
# Khởi tạo lớp, đối tượng
class Clock:
    def __init__(self, s, m, h):
        self.s = s
        self.m = m
        self.h = h
    # xây dựng hàm hiển thị mặt đồng hồ
    def clock_face(self):
        face = t.Turtle()
        face.hideturtle()
        face.penup()
        face.goto(0, -100)
        face.pencolor("blue")
        face.pensize(5)
        face.circle(100)
        face.penup()
        face.goto(0,0)
        face.speed(10)
        # vẽ vạch số chia trên mặt đồng hồ
        for i in range(13): # có 12 giờ
            for j in range(5):# có 5 phút trong 1 vạch giờ
                
                face.fd(95 - ((-j//5)+1)*5) # di chuyển đến vị trí vẽ vạch
                face.pendown()
                face.pensize(((-j//5)+1)*2+2) # mỗi vạch chia sẽ đậm hay nhạt hơn
                face.fd(((-j//5)+1)*5 + 5) # mỗi vạch chia sẽ ngắn, dài hơn ở vị trí cần
                face.penup()
                face.bk(100)
                face.rt(6)
    # Xây dựng hàm hiển thị kim giờ phút giây
    def clock_time(self):
        color = ["red", "brown", "black"]
        l_t = [self.s, self.m, self.h]
        show_time =[]
        # Dùng list để truy cập các phần tử thời gian trong nó
        for j in range(3): # j = theo thứ tự của kim giây, phút, giờ
            show_time = [270 + l_t[j]*(6+(j//2)*24)\
                    , j+1, 80-j*15, color[j]] # show_time = [góc quay, pensize, độ dài kim]
            j = t.Turtle()
            j.hideturtle()
            j.penup()
            #j.goto(0, 100)
            j.pendown()
            j.speed(10)
            j.rt(show_time[0])
            j.pencolor(show_time[3])
            j.pensize(show_time[1])
            j.fd(show_time[2])
# Vòng lặp vẽ liên tục trên mặt đồng hồ với thời gian thực
while True:
    # Đặt chính xác thời gian
    time = datetime.now()
    mics = time.microsecond 
    s = time.second
    m = time.minute
    h = time.hour
    s += mics/(10**6)
    m += s/60
    h += m/60       
    clock = Clock(s, m, h)
    clock.clock_face()
    clock.clock_time()
    
    
   
    


    