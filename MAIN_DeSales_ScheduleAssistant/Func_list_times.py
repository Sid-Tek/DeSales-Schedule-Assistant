from tkinter import*
from PIL import ImageTk,Image

global y_width
y_width = 5

def list_times():
    
    schedule_time = Label(text = "Schedule", bd=1, pady=y_width, relief = SUNKEN)
    schedule_time.grid(row = 0, column = 0, columnspan = 1, sticky=N+S)
    schedule_time.config(font=('Arial',25))

    schedule_time = Label(text = "Times     ", bd=1, pady=y_width, relief = SUNKEN,borderwidth=3)
    schedule_time.grid(row = 1, column = 0, columnspan = 1, sticky=N+S)
    schedule_time.config(font=('Arial',25))
    
    
    hour = 8
    displayed_hour = 8
    am_pm = "AM"
    row_num=2
    uniform_addition = ""

    
    while hour <= 14:
        uniform_addition = ""
        
        if hour == 12:
            am_pm = "PM"
        if hour >= 13:
            displayed_hour = hour - 12
        if displayed_hour < 10:
            uniform_addition = "  "
            
        
        schedule_time = Label(text = str(displayed_hour) + ":00 " + uniform_addition + am_pm, pady=y_width,bd=1, relief = SUNKEN,borderwidth=3)
        schedule_time.grid(row = row_num, column = 0, columnspan = 1, sticky=N+S)
        schedule_time.config(font=('Arial',25))
        
        schedule_time = Label(text = str(displayed_hour) + ":30 " + uniform_addition +am_pm, bd=1, pady=y_width, relief = SUNKEN,borderwidth=3)
        schedule_time.grid(row = row_num + 1, column = 0,columnspan = 1,sticky=N+S)
        schedule_time.config(font=('Arial',25))

        
        hour = hour + 1
        displayed_hour = hour
        row_num = row_num + 2
        uniform_addition = ""
    
    
    schedule_time = Label(text="3:00   PM", bd=1, pady=y_width, relief=SUNKEN,borderwidth=3)
    schedule_time.grid(row=row_num, column=0,columnspan = 1,sticky=N+S)
    schedule_time.config(font=('Arial',25))
