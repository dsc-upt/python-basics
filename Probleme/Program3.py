students = []

no_of_stud = input()

for i in range (int (no_of_stud)):
    student = {"Name": "0", "Age": 0, "Grade": 0}
    student["Name"] = input ("Nume: " )
    student["Age"] = int(input ("Age: " ))
    student["Grade"] = float(input("Grade: " )) 
    students.append(student)
print (students)
