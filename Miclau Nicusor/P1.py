size = 10
names = []
grade = []

for i in range(size):
    print("Enter name and grade")
    names.append(input())
    grade.append(int(input()))

students = dict(zip(names, grade))
print(students)