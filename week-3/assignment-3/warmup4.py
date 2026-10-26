
number =int(input("enter a number: "))

#sing block

if number < 0: 
  print (f"{number} is negative")
   
elif number  == 0:
  print (f"{number}is zero")
else:
  print(f"{number} positive")

#Parity block
if number % 2 == 0:  
  print (f"{number}is even")
else:
  print(f"{number} is odd")   

