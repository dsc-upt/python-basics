num_dict = int(input("Enter the number of dictionaries: "))
lst = []
for i in range(num_dict):
    student = {}
    student["name"] = input("Enter name: ")
    student["age"] = int(input("Enter age: "))
    student["grade"] = int(input("Enter grade: "))
    lst.append(student)
print(lst)