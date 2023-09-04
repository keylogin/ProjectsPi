import turtle

#create window and turtle
window = turtle.Screen()
chico = turtle.Turtle()

#draw stem and centre
chico.color("green", "black")
chico.left(90)
chico.forward(100)
chico.right(90)

#draw center colored
chico.begin_fill()
chico.circle(10)
chico.end_fill()

#draw all petals
for i in range(1, 24):
    if chico.color() == ("red", "black"):
        chico.color("blue", "black")
    elif chico.color() == ("blue", "black"):
        chico.color("yellow", "black")
    else:
        chico.color("red", "black")
    
    chico.left(15)
    chico.forward(50)
    chico.left(157)
    chico.forward(50)

#hide turtle
chico.hideturtle()


#tidy up window
window.exitonclick()
