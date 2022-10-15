from tkinter import* 
from PIL import ImageTk, Image
import pandas as pd, csv

import Schedules
import Func_Add_To_Schedule
import Func_Start_and_Length

#course = Label(text='l')
#course.config(font=('Arial','25'))
#course.grid(row=3,column=2,rowspan=5,sticky='nsew')
#info = course.grid_info()


# CS-115-01 and CS-260-01 are said to overlap WHEN THEY DON'T
# FIX THIS
def Find_Overlap(courseID):
    dataset = pd.read_csv('FALL 2022 DAY SCHEDULE.csv')
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
    
    # Rows occupied then day list
    
    i = 0
    addList = []
    while i < length:
        addList.append(startRow+i)
        i += 1
    addList.append(dayList)

    
    for element in Schedules.locationList:
        if dayList == element[len(element)-1]:
            i = 0
            while i < len(addList)-1:
                if addList[i] in element:
                    return True
                i += 1

    return False

#print(Schedules.schedule)
#print(Schedules.locationList)
#print(Find_Overlap('CS-260-01'))
