
import csv  # gives you the csv tools (DictReader lives here)

# '../data/students.csv' = the FILE on your computer (path to it)
# 'r' = read mode
# "as file" = a nickname for the open file, used inside the block
with open('../data/students.csv', 'r') as file:
    reader = csv.DictReader(file)  # reads each row as a dictionary
    for row in reader:             # row = one student at a time
        print(f"{row['name']}: {row['score']}")  # name: score