size = int(input())
names = []
grade = []
age = []
lst = []
for i in range(int(size)):
    print("Enter name, grade and age ")
    names.append(input())
    grade.append(int(input()))
    age.append(int(input()))
students = zip(names, grade, age)
lst.append(tuple(students))
print(lst)