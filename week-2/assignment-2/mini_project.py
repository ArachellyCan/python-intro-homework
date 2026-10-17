def Temperature_convert ():

    
    #1 Asks the user to ener a temperature in Fahrenheit.
    Temperature_fahrenheit = int(input ("what is the temperature in fahrenheit? "))
    Temperature_celsius = ((Temperature_fahrenheit-32)*5/9)
    
    
    print(f"the temperature in fahrenheit is {Temperature_fahrenheit} degrees")
    
    #2 Converts temperature in Celsius
    Temperature_celsius =int(input("what is the temperature in celsius? "))
    Temperature_fahrenheit = ( 32 +(9* Temperature_celsius/5)) 
    
    print(f"the temperature in celsius is {Temperature_celsius} degreesthe ")


Temperature_convert()
