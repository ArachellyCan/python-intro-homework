def calculate_age(age):
    if age <=12:
        print("Youare a Child")
    elif age <= 19:
        print("You are a Teenager")
    elif age <= 65:
        print ("You are an Adult")
    else:
        print("You are a Senior Citizen")

age= int(input("Enter your age:"))  
calculate_age(age)
       
         
            
