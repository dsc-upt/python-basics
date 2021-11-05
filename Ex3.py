numar=int(input("Alege numarul de studenti:"))
lst=[]
for k in range(numar):
    studentk={"Name": 0, "Age": 0,"Grade": 0}
    name=input("Numele studentului:")
    age=int(input("Varsta studentului:"))
    grade=int(input("Nota studentului:"))
    studentk["Name"]=name
    studentk["Age"]=age
    studentk["Grade"]=grade
    lst.append(studentk)
print(lst)

    
