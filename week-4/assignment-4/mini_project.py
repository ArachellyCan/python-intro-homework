day = input ("what day is it?").capitalize
time = input("what time of the day?").lower()
suggestion = "is a good time for python class!"

if day== "Tuesday" and "time" == "morning":
    print(f"{day}{time} {suggestion}")
elif day == "Tuesday" and "time"== "afternoon":
    print(f"{day}{time}{suggestion}")
else:
    print(f"{day}{time}{suggestion}")        
