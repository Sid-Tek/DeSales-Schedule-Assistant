from tkinter import* 
from PIL import ImageTk, Image
import pandas as pd, csv



    row = startRow
    rowspan = length
    i = 0
    addList = []
    while i < rowspan:
        addList.append(row+i)
        i += 1
    addList.append(Schedules.dayList)
    global overlapCheck
    overlapCheck = Func_Find_Overlap.Find_Overlap(addList)
    print(overlapCheck)
    if overlapCheck == False:
        Schedules.locationList.append(addList)
            
        for day in Schedules.dayList:
            course = Label(text=courseID,bg=color)
            course.config(font=('Arial','25'))
            course.grid(row=startRow,column=day,rowspan=output[0],sticky='nsew')
            info = course.grid_info()
            
    else:
        response = messagebox.showinfo("Error","Course overlaps with existing course")
