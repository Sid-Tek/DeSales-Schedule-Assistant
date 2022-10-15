from tkinter import*
from PIL import ImageTk,Image
import pandas as pd

import Func_Start_and_Length


global CSReq
CSReq = pd.read_csv('CSReq.csv')

# Add further major sheets here

global trackList
trackList = []

global locationList
locationList = []

global startingIDs
startingIDs = ['BI','CH','CJ','CM','CS']


# Add extra sheets in list below
global majorsList
majorsList = [CSReq]

for sheet in majorsList:
    i = 0
    for col in sheet.columns:
        if i > 2:
            trackList.append(col)
        i += 1


global track
track = 'Cyber Security'


global requiredCourses
requiredCourses = []

global schedule
schedule = []


def find_Track_List_Column_Name(name):
    for list in majorsList: 
        for column in list:
            if column == name:
                List = list
    column_Num = 0
    for column in List:
        if column == name:
            break
        else:
            column_Num += 1
    return List,column_Num,name

    
def updateRequiredCourses(name):
    requiredCourses.clear()
    trackList = []
    majorChosen = find_Track_List_Column_Name(name)
    List = majorChosen[0]
    column = majorChosen[1] 
    rowMax = len(majorChosen[0])
    name = majorChosen[2]
    
    i = 0
    while i < rowMax:
        course = List.iloc[i,column]
        if course == 'X':
            requiredCourses.append(List.iloc[i,0])
            
        i += 1
    

#updateRequiredCourses(track)

#Notify overlap
#requiredCourses = ['BI-257-01','CJ-109-03']

def replace_Course(old,new):
    i = 0
    while i < len(schedule):
        if schedule[i] == old:
            break
        else:
            i += 1
    schedule[i] = new

def Func_Fill_locationList():
    dataset = pd.read_csv('FALL 2022 DAY SCHEDULE.csv')
    for courseID in schedule:
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
        locationList.append(addList)
        

#Func_Fill_locationList()
#print(locationList)
