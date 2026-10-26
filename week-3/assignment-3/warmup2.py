def calculate_age(age):
    if age <=12:
        print("You are a Child")
    elif age <= 17:
        print("You are a Teenager")
    elif age <= 64:
        print ("You are an Adult")
    else:
        print("You are a Senior Citizen")

age= int(input("Enter your age: "))  
calculate_age(age)
       
         
            
