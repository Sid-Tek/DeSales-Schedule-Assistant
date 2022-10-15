from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image

import pandas as pd

from Func_list_times import*
import Func_list_times

from Func_list_days import*
import Func_list_days

from Func_Add_To_Schedule import*
import Func_Add_To_Schedule

from Func_List_Required_Courses import*
import Func_List_Required_Courses

import Schedules
from Schedules import*

import Func_Find_Overlap
import Func_Search_Course


from tkinter import messagebox

global dataset
dataset = pd.read_csv("FALL 2022 DAY SCHEDULE.csv")

#global timeSlotValue

global root
global main
main = Tk()
root = LabelFrame(main)
main.title("Schedule Assistant")
main.iconbitmap('Program_Logo.ico')



def updateWindow():
    
    Schedules.updateRequiredCourses(Schedules.track)
    
    Schedules.find_Track_List_Column_Name('Data Science')
    Schedules.locationList = []
    Schedules.Func_Fill_locationList()
    
    for widget in main.winfo_children():
        widget.destroy()

    screen_width = str(main.winfo_screenwidth())
    screen_height = str(main.winfo_screenheight())
    main.geometry(screen_width + "x" + screen_height)
        
    Func_list_times.list_times()
    Func_list_days.list_days()
    
    searchButton = Button(text='Search',command=lambda:Func_Search_Course.Search_Course())
    searchButton.grid(row=15,column=7,sticky='ew')
    
    clearButton = Button(text='Refresh',command=lambda:clearAll())
    clearButton.grid(row=16,column=7,sticky='e')
    
    insertButton = Button(text='Insert Course',command=lambda:insertCourse())
    insertButton.grid(row=16,column=7,sticky='w')
    
    global e
    
    e = Entry(main,width=9)
    e.grid(row=16,column=7)
    
    for element in Schedules.schedule:
        Func_Add_To_Schedule.Func_Add_To_Schedule(element)
    
        
    Func_List_Required_Courses.List_Required_Courses()
    
    rowNum = 0
    while rowNum != len(Schedules.requiredCourses):
    
        rowNum += 1
        
        
        addButton = Button(text='Add',command=lambda row=rowNum:addCourse(row))
        addButton.grid(row=rowNum,column=7,sticky='nw')
        
        removeButton = Button(text='Remove',command=lambda row=rowNum:removeCourse(row))
        removeButton.grid(row=rowNum,column=7,sticky='ne')
    
   
def insertCourse():
    # Input CS-115-02
    #If CS-115 is in the string, append Cs-115-02 to idData
    courseID = e.get()
    idData = []
    r = 0
    while r < len(dataset):
 
        idData.append(dataset.iloc[r,0])
        
        x = dataset.iloc[r,0]
        x = str(x)
        if x in courseID:
            idData.append(courseID)
            
        r += 1
    
    overlapCheck = Func_Find_Overlap.Find_Overlap(courseID)
    
    if courseID in idData and overlapCheck == False:
        shortCourseID = courseID[0:len(courseID)-3]
        Schedules.schedule.append(courseID)
        Func_Add_To_Schedule.Func_Add_To_Schedule(courseID)
        updateWindow()
        
    elif overlapCheck == True:
        message = messagebox.showinfo("Error","Course overlaps with existing course")    
    else:
        message = messagebox.showinfo("Error","No Course with that ID exists")    

def clearAll():
    Schedules.schedule = []
    updateWindow()

def addCourse(row):
    courseID = Schedules.requiredCourses[row-1]
    #if len(courseID == 6):
     #   slot = Func_Return_Course_TimeSlot.Return_Course_Timeslot(courseID)
      #  courseID = courseID + slot
    # Find_Overlap returns true or false based on ID
    
    overlapCheck = Func_Find_Overlap.Find_Overlap(courseID)

    if courseID in Schedules.schedule:
        message = messagebox.showinfo("Error","Course already added to schedule")
    if overlapCheck == True:
        message = messagebox.showinfo("Error","Course overlaps with existing course")    
    else:
        Schedules.schedule.insert(row-1,courseID)
        updateWindow()
        
def removeCourse(row):
    courseID = Schedules.requiredCourses[row-1]

    if courseID in Schedules.schedule:
        Schedules.schedule.remove(courseID)
        updateWindow()
    else:
        message = messagebox.showinfo("Error","Course already removed from schedule")
            


updateWindow()
root.mainloop()