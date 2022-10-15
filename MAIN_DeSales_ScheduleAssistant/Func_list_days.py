from tkinter import*
from PIL import ImageTk,Image


global x_width
x_width = 20

def list_days():

    schedule_day = Label(text = "Day    ", bd=1, relief = SUNKEN,padx=x_width,borderwidth=3)
    schedule_day.grid(row = 0, column = 1, columnspan = 1, sticky=W+E)
    schedule_day.config(font=('Arial',25))
    

    col_num=2
    
    day_list = ['Monday   ', 'Tuesday  ', 'Wednesday', 'Thursday  ', 'Friday   ']
    
    for string in day_list:
        schedule_day = Label(text=string, bd=1, relief = SUNKEN,padx=x_width,borderwidth=3)
        schedule_day.grid(row=0, column = col_num, columnspan=1,sticky=W+E)
        schedule_day.config(font=('Arial',25))
        col_num = col_num + 1
        
        

    