import turtle
turtle.bgcolor("light green")
h = turtle.Turtle()
s = turtle.Turtle()
t = turtle.Turtle()

h.pencolor("")  # không lộ màu trên đường di chuyển
h.goto(-200,-200)
h.pencolor("black")
m = 0

while m<2:
    if m == 0:
        h.fillcolor("blue") # chọn màu nền khung lớn
        
    elif m == 1:
        h.fillcolor("green")  # chọn màu nền khung nhỏ
       
    h.begin_fill()
    for j in range(2):
        
        for i in range(3):  # sử dụng vòng lặp để vẽ hình:
            x = (130/(m+1.6))*(i%2+(0.7/(m+1))) # kích thước phụ thuộc vào số vòng lặp và tính chẵn lẻ của i         
            h.fd(x)         # vòng while để chạy cửa ra vào ở lần khi m=1
            h.lt(90)                 # vòng for 1 để tạo nửa khung dạng ] khi j =0 và [ khi j =1
        j += 1                       # vòng for 2 để tạo 3 cạnh (1/2) hình chữ nhật [, ]
        h.rt(90)
        
    m += 1
    h.end_fill()
h.pencolor("")
h.goto(-256.875,-61.875)
h.pencolor("black")
corner = [-45,90,-70,115,65,115] # sử dụng list để truy cập các góc rẽ cho các cạnh
edge = [80.43,138.125]       # sử dụng list để truy cập các kích thước cho các cạnh
e = 0

for i in range(len(corner)): # vẽ mái và mặt bên của ngôi nhà
        
    if i == 0:          # phần mái trước với màu hồng
        h.fillcolor("pink") 
        h.begin_fill()
    elif i == 2:
        h.end_fill()
        h.fillcolor("yellow") # phần mặt bên màu vàng
        h.begin_fill()
    elif i == 5:
        h.end_fill()   
    if (i == 3) or (i == 5):
        e = edge[1]
    else:
        e = edge[0]
    h.rt(corner[i])
    h.fd(e)
   
    
h.pencolor("")
h.goto(-200,-5) 
h.pencolor("black")
h.fillcolor("orange") # Phần mái bên với màu cam
h.begin_fill()
h.rt(65)
h.fd(edge[0])
h.rt(70)
h.fd(edge[0])
h.rt(110)
h.fd(edge[0])
h.end_fill()
h.pencolor("")
h.goto(-90,-125)
h.pencolor("black")
cor = [115,65] # tạo list về kích thước góc
h.fillcolor("violet") # ô cửa sổ với màu tím
h.begin_fill()
for i in range(4):  # tạo ô cửa sổ hcn ngôi nhà
    h.fd((i%2+1)*25)
    h.rt(cor[i%2])
h.end_fill()
h.pencolor("")
h.home()

s.pencolor("")
s.goto(100,100)
s.pencolor("black")

for i in range(8): # sử dụng vòng lặp để vẽ hình tia nắng mặt trời:
    x = 40+10*(i%2+1) #  với mỗi i được một cạnh 
    s.rt(45) # kích thước của cạnh sử dụng tính chẵn lẻ của i
    s.fd(x) # mỗi lần quay phải được cạnh mới
    s.bk(x) # sau mỗi nét vẽ lại trở lại vị trí tâm
s.goto(100,61)
s.pencolor("black")
s.fillcolor("yellow")
s.begin_fill()
s.circle(40)
s.end_fill()
s.pencolor("")
s.home()

t.pencolor("")
home_t = [180,-120]
t.goto(home_t)
t.pencolor("black")
distance = [30,30*(2**(1/2))]
t.fillcolor("green")
t.begin_fill()
for i in range(6):       # vẽ cây thông
    t.fd(distance[i//3]) # sử dụng 6 vòng lặp cho 2 lần của 3 nhánh cây
    t.lt(135)            # sử dụng phép chia lấy phần nguyên để truy suất 
    t.fd(distance[(i//3) - 1])# phần tử trong distance (dis[0],dis[-1],dis[1],dis[0])
    t.rt(135)            # theo chiều tăng của i
    if i == 2:
        t.rt(135) # khi hết vòng lặp nó vẫn nhớ vị trí này thì phải???
t.end_fill() 
t.fillcolor("brown")     
t.begin_fill()
t.lt(135)   # để quay lại hướng ban đầu
for j in range(2):      # vẽ chân cây thông (tương tự như vẽ cửa ra vào ngôi nhà)
    for i in range(3):  # sử dụng vòng lặp để vẽ hình:
        x = 30*(i%2+0.5) # kích thước phụ thuộc vào số vòng lặp và tính chẵn lẻ của i         
        t.fd(x)         
        t.rt(90)         # vòng for 1 để tạo nửa khung dạng ] khi j =0 và [ khi j =1
                        # vòng for 2 để tạo 3 cạnh (1/2) hình chữ nhật [, ]
    t.lt(90)
t.end_fill()
t.pencolor("")
t.home()
turtle.done()
