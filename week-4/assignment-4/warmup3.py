#Create the lists 
language_programs_1 = ["C++", "Python", "Html", "CSS", "JaveScript", "Java"]
language_programs_2 = ["SQL", "R", "JavaScript", "C++", "Ruby", "C", "Html", ]

#Convert each list to a set with set()
set_1 = set(language_programs_1)
set_2 = set(language_programs_2)

#print with the | symbol to print two sets into one new set with no duplicates
#the uniong symble | shift + \
print(set_1 | set_2)
