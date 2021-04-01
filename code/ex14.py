import turtle

turtle.speed('fast')

def onePiece(n):
    if n <= 10:
        turtle.forward(n)
    else:
        onePiece(n / 3)
        turtle.left(60)
        onePiece(n / 3)
        turtle.right(120)
        onePiece(n / 3)
        turtle.left(60)
        onePiece(n / 3)


turtle.penup()
turtle.goto(-350, 0)
turtle.pendown()
onePiece(600)


turtle.done()
