from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("Radio Buttons")

#r = IntVar()
#r.set("2")

TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Corn","Corn"),
    ]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)
    


def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()


#Radiobutton(root,text="Option 1",variable=r,value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: clicked(r.get())).pack()

myLabel = Label(root,text=pizza.get())


myButton = Button(root,text="Add",command=lambda:clicked(pizza.get()))
myButton.pack()


mainloop()