import json 
text = input("Enter names and grades: ")
students = []
for student in text.split(","):
    name, gpa = student.strip().split()
    gpa = float(gpa)
    students.append({ "name": name, "gpa": gpa })
with open ("students.json", "w") as f:
    json.dump(students, f)