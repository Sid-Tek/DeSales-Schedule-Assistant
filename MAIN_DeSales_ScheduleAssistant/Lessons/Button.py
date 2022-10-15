from tkinter import*
root = Tk()


e = Entry(root, width=30, borderwidth=10,fg="pink",bg="purple")
e.pack()
e.insert(0,"Input Here")


def myClick():
    hello = "Hello " + e.get() + "!"
    myLabel = Label(root, text=hello,fg="green",bg="black")
    myLabel.pack()


myButton = Button(root, text="Enter Name"(,padx = 20, pady = 20,
                  command=myClick, fg="red",bg="tan"))
myButton.pack()








root.mainloop()
