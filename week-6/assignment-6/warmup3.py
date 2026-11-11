# Part 1: Scope Example

#Define a function named create_name
def create_name():
    #create a local variable named name
    #This varible only exists inside the function
    #Therefore it is a LOCAL Variable
    
    name = "Maria"


#calling the funciton
create_name()

# This would not work because name is local to the function
#print (name)

# Error you would get:
# NameError: name 'name' is not defined


# Part 2: Using return
#Create a fucntion
def create_name():

    #Create a local variable
    name = "Maria"

    #Send the value back ro the main program
    return name
#save the returned value in my_name
my_name = create_name()

print(my_name)