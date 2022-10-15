from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image

import pandas as pd


global dataset
dataset = pd.read_csv('FALL 2022 DAY SCHEDULE.csv')


# Course ID is 6 digits, such as CS-115
def Return_Course_Timeslot(courseID):
    win = Tk()
    win.title('Time Slot Selection')
    win.iconbitmap('Program_Logo.ico')
    x = dataset
    
    # Find all rows containing courseID, create list of those IDs
    maxRows = dataset.shape[0]
    i = 0
    timeSlots = []
    while i < maxRows:
        x = dataset.iloc[i,0:1].values
        x = str(x[0])
        if courseID in x:
            timeSlots.append(x)
        i += 1

    # timeSlots is that list
    
    newTimeSlots = []
    for element in timeSlots:
        x = (element,element[len(element)-3:len(element)])
        newTimeSlots.append(x)
    
    
    # newTimeSlots used in loop to create Radiobuttons
    
    slot = StringVar()
    slot.set('-01')
    
    for text,mode in newTimeSlots:
        Radiobutton(win, text=text, variable=slot, value = mode).pack(anchor=W)
        
    def clicked(value):
        win.destroy()
        return(value)
        
    
    myButton = Button(win,text="Select",command=lambda:clicked(slot.get()))
    myButton.pack()
    
    mainloop()


