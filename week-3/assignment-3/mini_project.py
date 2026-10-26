day= input ("what day is it?").capitalize()
time = input("What time of day is it? ").lower()  

if day =="Monday" and time == "morning":
    print(f"{day} {time}: plan your week and set your goals.")
elif day =="Monday" and time =="afternoon": 
    print(f"{day} {time} focus on your hardest assignment.")
elif day == "Monday" and time == "evening":
     print(f"{day} {time} review what you learn today.") 
elif day == "Tuesday" and time == "morning":      
     print(f"{day} {time} a great day to start a ne topic.") 
elif day == "Tuesday" and time == "afternoon": 
     print(f"{day} {time} a good time to focus!.") 
elif day == "Tuesday" and time == "evening": 
     print(f"{day} {time} practice a new coding exercise!.") 
elif day == "Wednesday" and time == "morning": 
     print(f"{day} {time} review your notes!.")  
elif day == "Wednesday" and time == "afternoon":
     print(f"{day} {time} work on your project.")          
elif day == "Wednesday" and time == "evening":
     print(f"{day} {time} doing a good review.") 
else:
     print(f"Invalid input:{day} {time}. Enter Monday, Tuesday, or Wednesday, and morning, afternoon, or evening.")              
