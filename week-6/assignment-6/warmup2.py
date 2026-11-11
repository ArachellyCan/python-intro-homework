#defining a function that takes Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    result= ((celsius-32)* 5/9) 
    return result

#Defining a function that takes Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    result = ((fahrenheit*9/5)+32)
    return result
    
# be aware that by having the correct alignemnet variables celsius and fahrenheit were defined    
celsius = float(input("enter temperature in celsius"))
fahrenheit = float(input("enter temperature in fahrenheit: "))
    
    
  
print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")

