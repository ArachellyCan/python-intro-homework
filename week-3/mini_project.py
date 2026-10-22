day= input ("what day is it?").capitalize()
time = input("What time of day is? ").lower()  
suggestion= "waht time of the day"


if day =="Tuesday" and time == "morning":
    print(f"{day} {time} {suggestion}")
elif day =="Tuesday" and time =="afternoon": 
    print(f"{day} {time} is a good time to focus!")
else: 
    print(f"{day} {time} is a good time to study")
