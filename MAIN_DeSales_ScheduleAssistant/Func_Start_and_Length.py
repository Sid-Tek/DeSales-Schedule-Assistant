from tkinter import*
from PIL import ImageTk,Image

import pandas as pd
import math

import time
import datetime
from datetime import timedelta


def Start_and_Length(start,end):

    day_modeS = ''
    day_modeE = ''
    
    if "PM" in start:
        day_modeS = "PM"
    else:
        day_modeS = 'AM'
    if "PM" in end:
        day_modeE = 'PM'
    else:
        day_modeE = 'AM'
        
    # Change string times into hour and minute values to input
    
    startTime = start[0:len(start)-2]
    startColonPosition = startTime.find(':')
    startHour = startTime[0:startColonPosition]
    startHour = int(startHour)   

    if startHour < 12 and day_modeS == 'PM':
        startHour += 12

    startMin = start[startColonPosition+1:startColonPosition+3]
    startMin = int(startMin)
    
    
    endTime = end[0:len(end)-2]
    endColonPosition = endTime.find(':')
    endHour = endTime[0:endColonPosition]
    endHour = int(endHour)

    
    endMin = end[endColonPosition+1:endColonPosition+3]
    endMin = int(endMin)
    
    if endHour < 12 and day_modeE == 'PM':
        endHour += 12
    
    if endMin == 50 or endMin == 45:
        endMin = 0
        endHour += 1
        

    startTime = datetime.datetime(1,1,1,startHour,startMin,0,0)
    endTime = datetime.datetime(1,1,1,endHour,endMin,0,0)


    length = (endTime - startTime)
    
    
    # Convert length to string, find hour and minute values
    
    startingHour = startTime.hour
    startMin = startTime.minute
    endHour = endTime.hour
    endMin = endTime.minute
    
    diff_Hour = endHour - startHour
    diff_Min = endMin - startMin

    
    length = (2*diff_Hour) + 1
    if diff_Min != 0:
        length += 1
    
    return length,startingHour,startMin,day_modeS

#print(Start_and_Length('1:00PM', '1:50PM'))
# CJ-109-03,Crime and Society TR 11:00AM 12:15PM
