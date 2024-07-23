import turtle
import time


ukuranfont = 18

# sets background
bg = turtle.Screen()
bg.bgcolor("blue")

pen = turtle.Turtle()

turtle.hideturtle()
# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("pink")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
    turtle.end_fill()
    

# Happy Birthday message

def tulis(pesan, pos):
    x,y=pos
    pen.penup()
    pen.goto(x,y)
    pen.color('white')
    style=('Stencil Std', ukuranfont, 'italic')
    pen.write(pesan, font=style)
    
def pesan(pesan, pos):
    x,y=pos
    pen.penup()
    pen.goto(x,y)
    pen.color('white')
    style=('Stencil Std', ukuranfont, 'italic')
    pen.write(pesan, font=style)

tulis('H',(-150.9,200))
time.sleep(0.1)
tulis('A',(-135,200))
time.sleep(0.1)
tulis('P',(-120,200))
time.sleep(0.1)
tulis('P',(-105,200))
time.sleep(0.1)
tulis('Y',(-90,200))
time.sleep(0.1)
tulis('B',(-60,200))
time.sleep(0.1)
tulis('I',(-45,200))
time.sleep(0.1)
tulis('R',(-40,200))
time.sleep(0.3)
tulis('T',(-25,200))
time.sleep(0.1)
tulis('H',(-10,200))
time.sleep(0.1)
tulis('D',(6,200))
time.sleep(0.3)
tulis('A',(21,200))
time.sleep(0.1)
tulis('Y',(36,200))
time.sleep(0.1)
tulis('老',(61,200))
time.sleep(0.1)
tulis('公',(85,200))
time.sleep(0.1)
tulis('长',(-150.9,170))
time.sleep(0.3)
tulis('寿,',(-125,170))
time.sleep(0.1)
tulis('永',(-75,170))
time.sleep(0.3)
tulis('远',(-50,170))
time.sleep(0.1)
tulis('健',(-25,170))
time.sleep(0.1)
tulis('康,',(1,170))
time.sleep(0.1)
tulis('心',(45,170))
time.sleep(0.5)
tulis('想',(70,170))
time.sleep(0.1)
tulis('事',(95,170))
time.sleep(0.1)
tulis('成',(120,170))
time.sleep(0.3)
tulis('我希望你永远快乐',(-100,140))
time.sleep(0.9)
pesan('''我很爱你 <3''',(-95,80))
pesan('''I Hope You Always Happy''',(-150,40))
time.sleep(5)
