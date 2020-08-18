# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 09:40:38 2020

@author: Hailemichel Getu
"""

import pandas as pd
import datetime
class inputData:
        def __init__(self, skill, year, month): 
            self.skill = skill
            self.year = year
            self.month = month
                  
file_name = r'Site_Capacity.xlsx' #initialize file path
df = pd.read_excel (file_name, sheet_name='Sheet1') #reading excel file to df variable
#Entering infinite loop


while(1):    
        #accepting string input for skill
        skill = input("Enter Skill: ")
        #accepting only 4 digit integer input for year with exception handling 
        while(1):
            #try accepting variable
            try:
                year = int(input("Enter Year: ")) #year variable is saved from the user
                if(year>1000 and year<9999): #check for 4 digit number, if yes, break while loop
                    break
                print("Invalid year input: ", year) #if not a 4 digit number, print this line and try accepting again
            except ValueError:
                print("Invalid year input! Try again...") #if exception happens print this line and try to accept inpu again
        #accepting only correct month input as integer with exception handling 
        while(1):   
                    #try accepting variable
            try:
                month = int(input("Enter Month: ")) #month  variable is saved from the user
                if(month>0 and month<=12): #check for proper month input, if yes, break while loop
                    break
                print("Invalid month input: ", month)#if not a proper month value, print this line and try accepting again
            except ValueError:
                print("Invalid month input! Try again...") #if exception happens print this line and try to accept inpu again
        datas = inputData(skill, year, month) #assigen datas variabl as inputData object with entered accepted data
        sSet = df[df["Skill"]==datas.skill].head()
        try:
            sSet2 = sSet[[datetime.datetime(datas.year, datas.month, 1)]]
            result = sSet2.sum(axis = 0,skipna = False)
            print(sSet2)
            print(result)
        except KeyError:
            print("Data not found based on the input. Please try again") #if exception happens print this line and try to accept inpu again
            continue
        




