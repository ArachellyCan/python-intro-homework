def Temperature_convert ():

    
    #1 Asks the user to ener a temperature in Fahrenheit.
    Temperature_fahrenheit = float(input ("what is the temperature in fahrenheit? "))
    
    #2 Converts the temperature in Celsius
    Temperature_celsius = ((Temperature_fahrenheit-32)*5/9)
    
    
   #3 Prints the result with 1 decimal
    print(f"{Temperature_fahrenheit:.1f}°F is {Temperature_celsius:.1f}°C.")


Temperature_convert()
