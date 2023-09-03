import turtle
import random

kaky = turtle.Turtle()
turtle.Screen().bgcolor("green")
colours = ["cyan", "purple", "white", "blue"]
kaky.penup()
kaky.forward(90)
kaky.left(45)
kaky.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            kaky.forward(30)
            kaky.backward(30)
            kaky.right(45)
        kaky.left(90)
        kaky.backward(30)
        kaky.left(45)
    kaky.right(90)
    kaky.forward(90)
    
for i in range(8):
    branch()
    kaky.left(45)
    
# for i in range(10):
#     kaky.color(random.choice(colours))
#     for i in range(2):
#         kaky.forward(100)
#         kaky.right(60)
#         kaky.forward(100)
#         kaky.right(120)
#     kaky.right(36)