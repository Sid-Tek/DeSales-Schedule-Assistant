from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")

def show():
        myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this box", variable = var, onvalue='on',offvalue='off')
c.deselect()
c.pack()



b = Button(root, text='Show selection', command=show).pack()



root.mainloop()