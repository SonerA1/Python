from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

label = Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10, pady=10)
label.pack()

def button_clicked():
    print("button clicked")
    print(text.get("1.0", END))


button = Button(text="button", command=button_clicked)
button.config(padx=10, pady=10)
button.pack()

entry = Entry(width=20)
entry.pack()

text = Text(width=30)
text.pack()


#scale
def scale_selected(value):
    print(value)


sclae = Scale(from_=0, to=50, command=scale_selected)
sclae.pack()

#spinbox
spinbox = Spinbox(from_=0, to=50)
spinbox.pack()

#checkbutton
checkbutton= Checkbutton(text="check")
checkbutton.pack()

#radiobutton
def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
radio_button = Radiobutton(text="1.option", value=10, variable=radio_checked_state, command=radio_selected)
radio_button2 = Radiobutton(text="2.option", value=20, variable=radio_checked_state, command=radio_selected)
radio_button.pack()
radio_button2.pack()


#Listbox

def listbox_selected():
    print(listbox.get(listbox.curselection()))

listbox = Listbox()
name_List = ["asd","abc","efg","asdasd"]
for i in range(len(name_List)):
   listbox.insert(i,name_List[i])

listbox.bind('<<ListboxSelect>>',listbox_selected)
listbox.pack()


window.mainloop()
