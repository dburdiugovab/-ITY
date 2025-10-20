from turtle import *
speed(0)
def draw_rectangle(x,y,color_draw,w,h):
    up()
    goto(x,y)
    down()
    color(color_draw)
    begin_fill()
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()
def sun(x,y,size):
    penup()
    goto(x,y)
    pendown()
    color('orange','yellow')
    begin_fill()
    for i in range(18):
        forward(size)
        left(100)
    end_fill()
draw_rectangle(-200,-200,' lightblue',400,400)#небо
draw_rectangle(-200,-200,'green',400,100)#трава
draw_rectangle(-150,-150, 'rosy brown',150,200)
x=-125
y=-135
for j in range(4):

    for i in range(2):
        draw_rectangle(x,y,'light pink',30,30)
        x+=70
    y+=50
    x=-125
draw_rectangle(80,-200 ,'grey',70,100)#дорога
draw_rectangle(110,-200,'white',10,100)#разметка
draw_rectangle(80,-200,'yellow',5,100)
draw_rectangle(145,-200,'yellow',5,100)
draw_rectangle(30,-100,'brown',10,40)#ствол
draw_rectangle(15,-60,'green',45,45)#листва
sun(120,120,60)#солнце


exitonclick()
hideturtle()
