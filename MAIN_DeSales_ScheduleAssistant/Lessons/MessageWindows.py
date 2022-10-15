from tkinter import *
from PIL import ImageTk,Image


def openSnake():   
    global img
    top = Toplevel()
    top.title("Snek")
    img = ImageTk.PhotoImage(Image.open('Snake.jpg'))
    lbl = Label(top, image=img).pack()
    button2 = Button(top, text="Close", command=top.destroy)





root = Tk()
root.title("Message Boxes")
root.iconbitmap('DeSalesLogo.ico')

button = Button(root, text="click for snake", command=openSnake)
button.pack()



mainloop()