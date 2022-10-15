from tkinter import*
from PIL import ImageTk,Image
import pandas as pd

def Find_Name(courseID):
    
    global dataset
    dataset = pd.read_csv("FALL 2022 DAY SCHEDULE.csv")
    
    if len(courseID) == 6:
        courseID = courseID + '-01'
    
    row_num = 0
    
    while 1==1:
        x = dataset.iloc[row_num , 0:1].values

        if courseID in x:
            x = dataset.iloc[row_num,1:2].values
            break
        else:
            row_num = row_num + 1
            
    x = x[0]
    return x

Find_Name('CS-115-02')