       
student = [{"name": "Melisa","grade":"A","Score": 98.0},
           {"name": "Gabriel","grade":"B","Score":90.00},
           {"name":"Jessy","grade":"B", "Score": 85.0},
           {"name":"Sonny","grade":"C", "Score": 79.0},
           ]
#average   code,unchanged)
total = 0 #the box holds 0
for person in student:
    total+= person["Score"]
average = total / len (student)
print(f"class average:{average}")

#total = 0   the box holds 0
#Round1:person is Melisa's dictionay
#total+= person["Score"] total = 0 + 98.0 = 98.0 
#Round2:person is Gabriel's dictionay
#total+= person["Score"] total = 98.0+90.0 = 188.0
#It continues for Jessy(273.0) and Sonny(352.0)then the loop stops
#average=total /len(student) 352.0/4 = 88.0


