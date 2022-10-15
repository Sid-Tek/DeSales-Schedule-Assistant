from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

img1 = ImageTk.PhotoImage(Image.open('Snake.jpg'))
img2 = ImageTk.PhotoImage(Image.open('Snake2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('Snake3.jpg'))

image_list = [img1, img2, img3]
image_num = 0


my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan = 3)

status_label = Label(root, text = "Image " + str(image_num+1) + " of "+ str(len(image_list)), bd=2, relief = SUNKEN, anchor=W)
status_label.grid(row=2, column = 0,columnspan=3, sticky=W+E)


def forward():
    global my_label
    global image_list
    global image_list_position
    global image_num
    global status_label
    
    if image_num != len(image_list)-1:
        image_num = image_num + 1
        my_label.grid_forget()
        my_label = Label(image=image_list[image_num])
        my_label.grid(row=0,column=0,columnspan = 3)
        
        status_label.grid_forget()
        status_label = Label(root, text = "Image " + str(image_num+1) + " of "+ str(len(image_list)), bd=2, relief = SUNKEN, anchor=W)
        status_label.grid(row=2, column = 0,columnspan=3, sticky=W+E)
        

def back():
    global my_label
    global image_list
    global image_list_position
    global image_num
    global status_label
    
    if image_num != 0:
        image_num = image_num - 1
        my_label.grid_forget()
        my_label = Label(image=image_list[image_num])
        my_label.grid(row=0,column=0,columnspan = 3)

        status_label.grid_forget()
        status_label = Label(root, text = "Image " + str(image_num+1) + " of "+ str(len(image_list)), bd=2, relief = SUNKEN, anchor=W)
        status_label.grid(row=2, column = 0,columnspan=3, sticky=W+E)



button_back = Button(root, text="<<", command= back)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward())


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1,pady=10)
button_forward.grid(row=1, column=2)



root.mainloop()