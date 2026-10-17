#1 What the errir message said 

age = "25"
next_year = age +
print(next_year)

#File "c:\Users\arace\python-intro-homework\week-2\assignment-2\warmup4.py", line 2, in <module>
#    next_year = age +1
#                ~~~~^~
#TypeError: can only concatenate str (not "int") to str

#2 what it caused it was the age variable contains a "25" string 
# next_year = age + 1
# when the math calculcation was suppoused to be done the concatenatin was not able to be done 
# since concatenation can not be done with strings 

#3 How you fix it

age = int("25")
next_year =age +1
print(next_year)

#3 since the issue was that the age was a string data type variable then I added the int data type 
#so the math calculation can be done.
#I could have just do age = 25, but I wanted to be more specific.


