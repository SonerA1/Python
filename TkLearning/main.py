<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b892eb4 (tkinter added)
>>>>>>> 9ac21cf (tkinter added)
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_right():
    turtle_instance.setheading(turtle_instance.heading()-50)
    #turtle_instance.right(10)

def rotate_left():
    turtle_instance.setheading(turtle_instance.heading() + 50)
    #turtle_instance.left(100)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key= "space")
drawing_board.onkey(fun=rotate_right, key= "Down")
drawing_board.onkey(fun=rotate_left, key= "Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="q")
drawing_board.onkey(fun=turtle_pen_down, key="w")

<<<<<<< HEAD
turtle.mainloop()
=======
<<<<<<< HEAD
turtle.mainloop()
=======
turtle.mainloop()
=======
import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
# window.minsize
window.minsize(width=450, height=300)

# label
my_label = tkinter.Label(
    # text=
    # fg=
    # bg=
    # width
    # height
    text="this is a label",
    font=('Arial', 30, "italic")
)

def click_button():
    user_input = my_entry.get()
    print(user_input)

# my_label.config(bg="black", fg="white")
#my_label.place(x=0, y=0)
#my_label.pack()
#my_label.pack(side="left")
#my_label.pack(side="top")
#my_label.pack(side="bottom")
my_label.grid(row=0, column=0)



# button
my_button = tkinter.Button(text="this is a button", command=click_button)
# my_button.place(x=225-63, y=150-14)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_width())
#my_button.pack()
#my_button.pack(side="left")
#my_button.pack(side="top")
#my_button.pack(side="bottom")
my_button.grid(row=1, column=1)

#entry
my_entry = tkinter.Entry(width=20)
#my_entry.place(x=300, y=200)
#my_entry.pack()
#my_entry.pack(side="left")
#my_entry.pack(side="top")
#my_entry.pack(side="bottom")
my_entry.grid(row=2,column=2)









window.mainloop()
>>>>>>> 61d2b59 (Tkinter)
>>>>>>> b892eb4 (tkinter added)
>>>>>>> 9ac21cf (tkinter added)
