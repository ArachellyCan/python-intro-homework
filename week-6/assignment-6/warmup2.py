# Defining a function that converts Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):

    # Formula: (C × 9/5) + 32
    result = ((celsius * 9/5) + 32)

    # Return the result to where the function was called
    return result


# Defining a function that converts Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):

    # Formula: (F - 32) × 5/9
    result = ((fahrenheit - 32) * 5/9)

    
    # Return the result to where the function was called
    return result


# Ask the user for a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Ask the user for a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))


# Call the celsius_to_fahrenheit function
# :.1f rounds the answer to 1 decimal place
print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.1f}°F")

# Call the fahrenheit_to_celsius function
# :.1f rounds the answer to 1 decimal place
print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.1f}°C")

