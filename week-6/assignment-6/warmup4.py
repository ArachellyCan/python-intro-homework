#definign a function with one parameter score
def is_valid_score(score):
    
    #start an if statement
    #check of score is greater thatn or equal to 0
    #less than or equal to 100
    if score >= 0 and score <= 100: 
        
        #if the contition is True, return True
        return True
    else:
        #otherwise return False
        return False
#Ask the user to enter a scoe
score = int(input("Enter a score: "))

#Call the function snd use its return value in an if statement
if is_valid_score(score):
    
    #Runs whwn the function returns True
    print("Valid score.")
else:
    
    #Runs when the funtion returns False
    print("Invalid score — must be between 0 and 100.")