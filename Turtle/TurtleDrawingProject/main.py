import turtle

drawing_bord = turtle.Screen() # screnn
drawing_bord.bgcolor("green") # color palet
drawing_bord.title("Python Turtle") # title

'''
turtle_instance = turtle.Turtle() # instance
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(45)
turtle_instance_2.forward(100)
'''
# draw square
'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
'''

'''
For loop
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)
'''

'''
# Star
turtle_instance = turtle.Turtle()
for i in range(8):
    turtle_instance.right(144)
    turtle_instance.forward(200)
'''

'''
# polyStar
turtle_instance = turtle.Turtle()
for i in range(9):
    turtle_instance.right(200)
    turtle_instance.forward(200)

'''

#polygon

turtle_instance = turtle.Turtle()
num_sides = 8
angle = 360.0 / num_sides
side_length = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()