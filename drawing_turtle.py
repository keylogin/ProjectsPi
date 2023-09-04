import turtle

#create window and turtle
window = turtle.Screen()
chico = turtle.Turtle()

#draw stem and centre
chico.left(90)
chico.forward(100)
chico.right(90)
chico.circle(10)

#draw all petals
for i in range(1, 24):
    chico.left(15)
    chico.forward(50)
    chico.left(157)
    chico.forward(50)

#tidy up window
window.exitonclick()
