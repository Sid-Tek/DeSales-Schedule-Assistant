from tkinter import*
from PIL import ImageTk,Image


root = Tk()
root.title("Icons, Images, Exit Buttons")

img = ImageTk.PhotoImage(Image.open('Snake.jpg'))
my_Label = Label(image=img)
my_Label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()











root.mainloop()