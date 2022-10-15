from tkinter import*
from PIL import ImageTk,Image
import pandas as pd

from Func_Find_Name import*
import Func_Find_Name

import Schedules
requiredCourses = Schedules.requiredCourses
schedule = Schedules.schedule


global checklist


def changeTrack(name):
    if name in Schedules.trackList:
        Schedules.track = name
        Schedules.updateRequiredCourses(name)
    else:
        response = messagebox.showinfo("Error","No major exists with that name")
    changePathWin.destroy()
    
def changePath(event):
    global changePathWin
    changePathWin = Tk()
    changePathWin.title('Change Track')
    changePathWin.iconbitmap('Program_Logo.ico')
    
    searchBox = Entry(changePathWin,width=30)
    searchBox.grid(row=0,column=0,columnspan=1,sticky='ew')
    
    confirmButton=Button(changePathWin,text='Change',command=lambda:changeTrack(searchBox.get()))
    confirmButton.grid(row=0,column=1,columnspan=1)
    


def List_Required_Courses():
    header = Label(text="Required Courses",borderwidth=1,relief='sunken')
    header.config(font=('Arial',25))
    header.grid(row=0,column=7,sticky='nsew')
    header.bind("<Button-1>",changePath)

    
    checklist = []
    
    global i
    i = 0
    
    global dataset
    dataset = pd.read_csv('FALL 2022 DAY SCHEDULE.csv')
    
    global maxRows
    maxRows = dataset.shape[0]
    
    global timeSlots
    timeSlots = []
    
    global sameCourses
    sameCourses = []
    
    global finalTimeSlots
    finalTimeSlots = []
    
    while i < maxRows:
        x = dataset.iloc[i,0:1].values
        x = str(x)
        timeSlots.append(x)
        i += 1
    

    # Have checklist include all possible iterations
    # Copy code from Return Course TimeSlots
    # Refine timeSlots to include courses that match requiredCourses
    i = 0
    while i < len(requiredCourses):
        
        for slot in timeSlots:
            x = str(slot)
            x = x[1:len(slot)-1]
            if requiredCourses[i] in x:
                sameCourses.append(x)
                
        checklist.append((requiredCourses[i],Func_Find_Name.Find_Name(requiredCourses[i])))
            
        i += 1
        
    for course in sameCourses:
        x = course[1:len(course)-1]
        finalTimeSlots.append((course,Func_Find_Name.Find_Name(x)))


    i = 0
    rowNum = 1
   

    while i < len(requiredCourses):
        color = '#FF7377'

        if len(Schedules.schedule) >= 1:
            for course in Schedules.schedule:
                if checklist[i][0] in course:
                    color = 'lightgreen'

        else:
            color = '#FF7377' # Light Red
        header = Label(text="\n\n"+checklist[i][0]+" - "+ checklist[i][1],borderwidth=1,relief='sunken',bg=color)
        header.config(font=('Arial',10))
        header.grid(row=rowNum,column=7,sticky='nsew')
        
        i += 1
        rowNum += 1
        # command=lambda:addCourse\

    
         
