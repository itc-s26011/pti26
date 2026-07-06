import turtle

# 画面
screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.width(2)

# 花びら
def petal():
    t.color("deeppink")
    t.begin_fill()
    for _ in range(2):
        t.circle(60, 60)
        t.left(120)
        t.circle(60, 60)
        t.left(120)
    t.end_fill()

# 桜（5枚の花びら）
for _ in range(5):
    petal()
    t.left(72)

# 花の中心
t.penup()
t.goto(0, -10)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(10)
t.end_fill()

# 茎
t.penup()
t.goto(0, -10)
t.setheading(-90)
t.pendown()
t.color("brown")
t.width(5)
t.forward(120)

t.hideturtle()
turtle.done()
