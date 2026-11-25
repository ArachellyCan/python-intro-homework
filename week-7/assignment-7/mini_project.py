#cvs = tools for reading CSV files
#OS = tools for checking files and folders
#sys = lets us stop the program with sys.exit ()
#datetime = gives us today's date
import csv
import os
import sys
from datetime import datetime

#Build the path to the datea file (Step 1 uses this)
path = os.path.join("..", "data","expenses.csv")

#STEP 1 stop if the file doesnt exist
if not os.path.exists(path):
    print("Error: expenses.csv not found.")
    sys.exit() #stops the progarm here

#STEP 2: read the CSV into a list of dictionaries
#Each row looks like {'date': '2024-03-01', 'category': 'Food'...}
with open(path, 'r')as file:
    reader = csv.DictReader(file)
    rows = list(reader)    #list () collects every row into one list

#STEP 2: read the CSV into a list of dictionaries
#Each row looks like {'date': '2024-03-01' , 'category': 'Food' , ...}
with open (path,'r')as file:
    reader = csv.DictReader(file)
    rows = list(reader)  #list () collects every row into one list

#STEP 3: concert amung from text to a number
#DictReader gives back strings. so math wont unitl we use float()

for row in rows:
    row['amount'] = float(row['amount'])

#STEP 4: keep only hte rows where category is "Food"  
food_rows =[]
for row in rows:
    if row['category'] == "Food":
        food_rows.append(row)

#STEP 5: add up the food amounts
total = 0
for row in food_rows:
    total =  total + row['amount']

#STEP 6: write the report to food_report.txt
#'w' creates the file ( or overwrites it if it already exists)
#encoding = 'uft-8' makes sure the long dash (-)saves correctly on Windows
today = datetime.now ().strftime ("%B %d, %Y")

with open('food_report.txt', 'w', encoding='utf-8') as report:
    # First line: title with today's date
    report.write(f"Food Expense Report — generated {today}\n")

    # One line per food expense: date: $amount
    for row in food_rows:
        report.write(f"{row['date']}: ${row['amount']:.2f}\n")

    # Last line: the total with 2 decimal places
    report.write(f"Total: ${total:.2f}\n")


   
    