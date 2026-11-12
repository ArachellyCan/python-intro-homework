#def greet(name):
    #print("Hello," + name +  "!")
    #print("Good morning, "+ name)
    #print("Welcome,"+ name + "!")

#greet("Alex")    


# Define a function with two parameters:
# name and greeting
# greeting has a default value of "Hello"
#Define a function named greet
def greet(name, greeting="Hello"):

    # Print the greeting and the name
    print(greeting + ", " + name + "!")

# Call #1
# Only pass a name
# Python uses the default greeting: "Hello"
greet("Alex")

# Call #2
# Pass both values in order
# name = "Alex"
# greeting = "Good morning"
greet("Alex", "Good morning")

# Call #3
# Pass the greeting by using its parameter name
# greeting = "Welcome"
greet("Alex", greeting="Welcome")