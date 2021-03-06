'''
Creators: Robb Blain, Ethan Blow
Sources: codeHS, stack overflow, Mr.Lange
Description: Make a "turtle" draw a truck color it in and add details, then aks if you liked it
'''

# main turtle
import turtle

#dave = turtle.Turtle()
wn = turtle.Screen()
alex = turtle.Turtle()

def winders():
    alex.penup()
    alex.left(135)
    alex.forward(58)
    alex.left(90)
    alex.pendown()
    alex.forward(53)
    alex.right(90)
    alex.forward(55)
    alex.right(90)
    alex.forward(53)
    alex.right(90)
    alex.forward(55)
    alex.penup()
    alex.left(180)
    alex.forward(65)
    alex.left(90)
    alex.pendown()
    alex.forward(53)
    alex.right(90)
    alex.forward(65)
    alex.right(45)
    alex.forward(35)
    alex.right(45)
    alex.forward(30)
    alex.right(90)
    alex.forward(88.5)
    alex.penup()


def drawbed():
    alex.penup()
    alex.left(90)
    alex.forward(77.5)
    alex.left(90)
    alex.forward(212)
    alex.right(90)
    alex.forward(38)
    alex.pendown()
    alex.left(135)
    alex.forward(52)
    alex.left(180)
    alex.forward(53)
    alex.left(45)
    alex.forward(10)
    alex.left(135)
    alex.forward(68)


def drawwheel():
    alex.pendown()
    for i in range(240):
        alex.forward(1)
        alex.left(1.5)
    alex.penup()


def drawinwheel():
    for i in range(144):
        alex.forward(1)
        alex.left(2.5)


def bfender():
    alex.left(90)
    for i in range(180):
        alex.forward(0.75)
        alex.right(1)


def ffender():
    alex.left(90)
    for i in range(180):
        alex.forward(0.75)
        alex.right(1)


# start
alex.penup()
alex.setposition(-110, -195)
alex.speed(0)
'''
# wheels
# outerwheels
# 1
alex.pendown()
drawwheel()
# 2
alex.setposition(100, -195)
drawwheel()

# innerwheels
# 1
alex.penup()
alex.setposition(-110, -180)
alex.pendown()
drawinwheel()
# 2
alex.penup()
alex.setposition(100, -180)
alex.pendown()
drawinwheel()

# rims
# 1
for i in range(18):
    alex.penup()
    alex.setposition(-110, -158)
    alex.pendown()
    alex.forward(22)
    alex.left(20)
# 2
for i in range(18):
    alex.penup()
    alex.setposition(100, -158)
    alex.pendown()
    alex.forward(22)
    alex.left(20)
'''
# bottom
# back
alex.penup()
alex.setposition(-175, -135)
alex.pendown()
alex.forward(20)
bfender()
# front
alex.left(90)
alex.forward(125)
ffender()

# front
alex.left(90)
alex.forward(20)

for i in range(90):
    alex.forward(0.375)
    alex.left(0.5)
alex.left(45)
alex.forward(40)

for i in range(90):
    alex.forward(0.375)
    alex.left(0.5)

# hood/windsheild
alex.left(45)
alex.forward(65)
alex.right(45)
alex.forward(75)

# roof/bed
alex.left(45)
alex.forward(150)
alex.left(90)
alex.forward(60)
alex.right(90)
alex.forward(110)
alex.left(90)
alex.forward(77.5)
alex.left(90)
alex.forward(22)

# bedbars
alex.penup()
alex.forward(300)
alex.pendown()
drawbed()

# draw windows
winders()

#colour
#front
alex.pencolor("red")
alex.setposition(171,-132)
alex.pendown()
alex.forward(28)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(31)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(5)
alex.left(180)
alex.forward(36)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(36)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(2)
alex.left(180)
alex.forward(38)
alex.right(90)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.left(180)
alex.forward(41)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(2)
alex.left(180)
alex.forward(43)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(44)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(2)
alex.left(180)
alex.forward(46)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(48)
alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(49)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(50)
alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(50)
for i in range(24):
    alex.right(90)
    alex.forward(1)
    alex.right(90)
    alex.forward(50)
    alex.left(90)
    alex.forward(1)
    alex.left(90)
    alex.forward(50)
for i in range(2):
    alex.right(90)
    alex.forward(1)
    alex.right(90)
    alex.forward(49)
    alex.left(90)
    alex.forward(1)
    alex.left(90)
    alex.forward(49)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(48)
alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(48)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(47)
alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(47)
alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(47)
alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(47)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(45)
alex.backward(1)

alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(1)
alex.left(180)
alex.forward(45)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(45)
alex.backward(1)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(44)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(43)
alex.backward(1)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(42)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(41)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(41)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(41)
alex.backward(1)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(40)
alex.backward(1)

alex.forward(1)
alex.left(90)
alex.forward(70)

alex.right(180)
alex.forward(3)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(67)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(65)

alex.right(180)
alex.forward(3)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(62)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(60)

alex.right(180)
alex.forward(2)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(58)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(57)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(56)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(55)

alex.right(180)
alex.forward(2)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(53)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(52)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(51)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(50)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(49)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(48)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(47)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(47)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(46)

alex.left(90)
alex.left(90)
alex.forward(45)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(45)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(45)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(44)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(43)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(43)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(42)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(42)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(41)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(41)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(41)

alex.right(180)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(40)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(40)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(40)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(39)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(39)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(39)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(39)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

alex.right(180)
alex.left(90)
alex.forward(1)
alex.right(90)
alex.forward(38)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(38)

#midddle
alex.right(90)
alex.forward(1)
alex.left(90)
alex.forward(1)
alex.right(180)
alex.forward(39)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(39)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(39)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(39)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(39)

alex.left(90)
alex.forward(1)
alex.left(90)
alex.forward(40)

alex.right(90)
alex.forward(1)
alex.right(90)
alex.forward(40)
















# end
alex.penup()
alex.forward(500)

turtle.done()

like = -5
while like < 1 or like > 3:
    try:
        like = float(input('Did you like my truck?(1 = yes 2 = No) '))

    except ValueError:
        print('1 or 2')

if like == 1:
    print('Thank you')

if like == 2:
    print('wow I see how it is no more pictures for you')