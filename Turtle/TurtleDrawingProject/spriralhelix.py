import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("orange")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

for i in range(10):
    #turtle_instance.circle(100)
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)


turtle.done()