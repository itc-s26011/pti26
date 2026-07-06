import turtle

# 画面設定
screen = turtle.Screen()
screen.bgcolor("lightskyblue")

t = turtle.Turtle()
t.speed(0)
t.width(2)

# 桜の花びら
def petal():
    t.color("hotpink")
    t.begin_fill()

    t.left(20)
    t.circle(40, 60)
    t.left(120)
    t.circle(40, 60)
    t.left(20)

    t.end_fill()

# 桜の花
def sakura(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    for _ in range(5):
        petal()
        t.left(72)

    # 花の中心
    t.penup()
    t.goto(x, y - 5)
    t.color("gold")
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# 枝
t.penup()
t.goto(-250, -50)
t.setheading(20)
t.color("saddlebrown")
t.width(8)
t.pendown()
t.forward(220)

# 小枝
t.backward(100)
t.left(50)
t.forward(70)

t.backward(70)
t.right(100)
t.forward(80)

# 花を描く
sakura(-80, 20, 6)
sakura(0, 70, 6)
sakura(70, 10, 6)
sakura(-10, -20, 6)

t.hideturtle()
turtle.done()
