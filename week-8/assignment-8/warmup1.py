#WITH try/except:

try:
    number = float(input('Enter a number: '))
except ValueError:
    print("That is not a valid number. Try again. ")    

#User types: hello
#Result: No crash. Python catches the error and prints message