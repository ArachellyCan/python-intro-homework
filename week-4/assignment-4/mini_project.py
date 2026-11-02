       
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#AVERAGE
total = 0 #the box holds 0
for person in students:
    total+= person["score"]
average = total / len (students)
print(f"class average:{average}")


top_name = None #creating a variable thta currently has no value
top_score = 0 #crating a varable that stars at zero/ it needs to have a starting point
#befor comparing the students score

#TOP SCORE 
for person in students:
    if person["score"]> top_score:# we create a cyc
        top_score = person["score"]#updates the varaible when python finds a higher score

        top_name =person["name"]#remembers the name of the student who has the score

print(f"Top scorer:{top_name}with{top_score}")

#UNIQUE SUBJECTS
subjects = set ()
for person in students:
    subjects.add (person["subject"])
print(f"subjects offered:{subjects}")    

#HIGH SCORER PER SUBJECT
high_scorers = []
for person in students:
    if person["score"] > 75:
        high_scorers.append(person["name"])

print(f"high_scorers:{high_scorers}")
        