#import = bring in a toolbox of ready-made tools
#os = the toolbox for working with files and folders
#This must come FIRST, before any line that uses "os"

import os

#Part 1: PRINT THE CURRENT WORKING DIRECTORY
#os.getcwd() = "get current working directory"
#IT returns the folder Python is running from, as text
#print () shows that text on the screen
print(os.getcwd())

#PART 2: CHECK IF THE FILE EXISTS
#os.path.exists(..) checks if a file or folder is really there
#it gives back True (it exists) or False )it doesn't)
# Teh path '../data/expenses.csv' means:
#..    = go up one folder
#data  = open the data folder
#expenses.csv   =the file inside it

if os.path.exists('../data/expenses.csv'):
    #runs only when the amswer was True
    print("expenses.csv found.")   
else:
    #runs only when the answer was False
    print("expenses.csv not found.")

#PART 3:
# os.path.join() glues the pieces together into one path
# The pieces are: "..", "data", "expenses.cvs" )
#
path = os.path.join(".." , "data", "expenses.csv")

#print() shows the path that was built
print(path)
                    