#from datetime import datetime = bring in the datetime tool form the datetim toolbox

from datetime import datetime
#datetime.now() = the current date and time. form your computer's clock
today = datetime.now()

#.strftime() turns the date into text in the format you choose
#The % code are placeholders that get replaced by real values:
#%B = full month name (Novemeber)
#%d =day of the moth as a number (23)
#Y = four digit year (2026)
#Everything else (the world "Today is", the comma, the period) is printed as written
formatted = today.strftime("Today is %B %D, %Y")

#print() shows the finished sentence
print (formatted)

