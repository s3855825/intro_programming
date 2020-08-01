import turtle

# start with blue background, then fill in white and red stripes.
turtle.color("blue")
turtle.begin_fill()
turtle.penup()
turtle.setx(-125)
turtle.sety(125)
turtle.pendown()
turtle.forward(500)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

turtle.exitonclick()
