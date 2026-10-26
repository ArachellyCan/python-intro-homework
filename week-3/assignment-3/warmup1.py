def grade_calculator(score):
    if score >=90:
        print("Grade: A")
    elif score >= 80:
        print("Grade:B")
    elif score >= 70:
        print("Grade: C") 
    elif score>=60:    
        print("Grade: D")

    elif score<= 60:
        print("Grade: F")   
score = int(input("Enter your sccore: "))
grade_calculator(score)     