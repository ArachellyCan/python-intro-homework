#Create the lists 
language_programs_1 = ["C++", "Python", "Html", "CSS", "JavaScript", "Java"]
language_programs_2 = ["SQL", "R", "JavaScript", "C++", "Ruby", "C", "Html", ]

#Convert each list to a set with set()
set_1 = set(language_programs_1)
set_2 = set(language_programs_2)

#print with the | combines two sets into one new set,
#printing both lines in a single result with out repeating results
#the uniong symble | shift + \
print(set_1 | set_2)#union
print(set_1 & set_2)#intersection
print(set_1 - set_2)#difference
