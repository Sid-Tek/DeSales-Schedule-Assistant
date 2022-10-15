from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")


frame = LabelFrame(root,padx=10,pady=10)
frame.pack(padx=10,pady=10)


b = Button(frame, text="press")
b.grid(row=0,column=0)

b2 = Button(frame, text="Click")
b2.grid(row=0,column=1)


root.mainloop()