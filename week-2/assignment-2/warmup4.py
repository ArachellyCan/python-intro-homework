#1 What the error message said 

#age = "25"
#next_year = age +
#print(next_year)

#File "c:\Users\arace\python-intro-homework\week-2\assignment-2\warmup4.py", line 2, in <module>
#    next_year = age +1
#                ~~~~^~
#TypeError: can only concatenate str (not "int") to str

#Python reds int ("25"). It takes the text "25" and convers it into the number 25.
#age= saves that number 25 in the variable age. From now on, age is not text anymore
#it is the number 25
#Python reads next_year = age +1 . It replaces age with its value, so it becomes 
#25 + 1


#3 How you fix it

age = int("25")
next_year =age +1
print(next_year)

#converteed the varible age into a int
#so the math calculation can be done.



