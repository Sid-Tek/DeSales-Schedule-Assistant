from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image
import pandas as pd
import Schedules


global dataset
dataset = pd.read_csv("FALL 2022 DAY SCHEDULE.csv")




def getResults(string):
    
    startingID = string[0:2]
    
    idList = []
    nameList = []

    if startingID in Schedules.startingIDs:
        # List all courses, ID + Name, starting with those 2 letters
        

        rowNum = 0
        while rowNum < len(dataset):
            x = dataset.iloc[rowNum,0]
            x = str(x)
            if startingID in x:
                idList.append(dataset.iloc[rowNum,0])
                nameList.append(dataset.iloc[rowNum,1])
            rowNum += 1    
      
    else:
        #List all courses, ID + Name, with those letters
        #Change input to lowercase
        
        string = string.upper()
        rowNum = 0
        
        while rowNum < len(dataset):
            x = dataset.iloc[rowNum,1]
            x = str(x)
            x = x.upper()
            if string in x:
                idList.append(dataset.iloc[rowNum,0])
                nameList.append(dataset.iloc[rowNum,1])
            rowNum += 1
                    
    

    
    if len(labels) >= 1:
        for label in labels:
            label.grid_forget()

    i = 0
    rowNum = 1
    while i < len(idList):
        label = Label(searchWin,text=idList[i]+" - "+nameList[i],pady=5)
        labels.append(label)
        label.grid(row=rowNum,column=0,columnspan=1,sticky='w')
        label.config(font=('Arial',15))
        i += 1
        rowNum += 1



def Search_Course():
    
    global searchWin
    searchWin = Tk()
    searchWin.geometry("1000" + "x" + str(searchWin.winfo_screenheight()))
    
    global labels
    labels = []
    
    global searchBox
    
    searchWin.title("Course Search")
    searchWin.iconbitmap('Program_Logo.ico')
    
    searchBox = Entry(searchWin,width=20)
    searchBox.grid(row=0,column=0,columnspan=1,sticky='ew')
    
    searchButton=Button(searchWin,text='Search',command=lambda:getResults(searchBox.get()))
    searchButton.grid(row=0,column=1,columnspan=1)
    
    

# DISPLAY DAYS AND TIMES
# STILL NEED SCROLLBAR    
    
