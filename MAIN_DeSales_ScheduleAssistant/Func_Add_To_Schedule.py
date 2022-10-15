from tkinter import* 
from PIL import ImageTk, Image
import pandas as pd, csv

import Func_Start_and_Length
import Func_Find_Name
import Func_Find_Overlap
import Schedules



def Func_Add_To_Schedule(courseID):
    global color
    global dataset
    dataset = pd.read_csv('FALL 2022 DAY SCHEDULE.csv')
    color = 'orange'
    if courseID[0:2] == 'BI':
        color = 'lightblue'
    if courseID[0:2] == 'CH':
        color = 'cadetblue'
    if courseID[0:2] == 'CJ':
        color = 'green'
    if courseID[0:2] == 'CM':
        color = 'wheat'
    if courseID[0:2] == 'CS':
        color = 'grey'
    
    
# Find different times course is offered (01,02,etc) and ask to choose    
# Setting this to -01 is a stopgap measure
    if len(courseID) == 6:
        courseID = courseID + '-01'



    row_num = 0
    #NO for row in dataset NO NO NO NO NO
    while 1==1:
        x = dataset
        x = x.iloc[row_num, 0:1].values
        if courseID in x:
            break
        else:
            row_num = row_num + 1
    
    #FIX THIS
    x = dataset
    date_Text = x.iloc[row_num, 2:3].values
    date_Text = date_Text[0]
    colonPos = date_Text.find(':')
    #print(colonPos)
    if date_Text.find('MWF') != -1:
        date_Text = date_Text[colonPos-6:len(date_Text)]
    else:
        date_Text = date_Text[colonPos-5:len(date_Text)]
    dayList = []
    if date_Text[0:3] == 'MWF':
        dayList = [2,4,6]
    else:
        dayList = [3,5]
    # Takes out days from date_Text
    u = date_Text.find(' ')
    date_Text = date_Text[u+1:len(date_Text)]
    
    
    startTime = date_Text[0:7]
    endTime = date_Text[8:len(date_Text)]
    
    if startTime[0] == '0':
        startTime = startTime[1:len(startTime)]
        
    if endTime[0] == '0':
        endTime = endTime[1:len(endTime)]
        


    output = Func_Start_and_Length.Start_and_Length(startTime,endTime)
    #output = (3,11,0,'AM')
    #return length,startHour,startMin,day_mode
    
    length = output[0]
    start_Hour = float(output[1])
    startRow = start_Hour * 2
    startRow -= 14
    startRow = int(startRow)
    

    for day in dayList: 
        course = Label(text=courseID,bg=color)
        course.config(font=('Arial','25'))
        course.grid(row=startRow,column=day,rowspan=output[0],sticky='nsew')
        info = course.grid_info()
        

#Func_Add_To_Schedule('CS-115-01')
#Func_Add_To_Schedule('CS-260-01')
# grid_remove()
