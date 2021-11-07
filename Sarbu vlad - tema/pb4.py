lst_main = []
for i in range(5):
    player = {}
    player["name"] = input("Enter player name: ")
    player["age"] = int(input("Enter player age: "))
    player["number"] = int(input("Enter player number: "))
    lst_main.append(player)

lst_reserve = []
for i in range(3):
    player = {}
    player["name"] = input("Enter reserve name: ")
    player["age"] = int(input("Enter reserve age: "))
    player["number"] = int(input("Enter reserve number: "))
    lst_reserve.append(player)

name_player = input("Enter the name of the player you want swapped: ")
name_reserve = input("Enter the name of the reserve you want swapped: ")

i = 0
while lst_main[i]["name"] != name_player:
    i += 1

j = 0
while lst_reserve[j]["name"] != name_reserve:
    j += 1
    
aux = {"name" : "", "age" : 0, "number" : 0}
aux = lst_main[i]
lst_main[i] = lst_reserve[j]
lst_reserve[j] = aux

print(lst_main)
print(lst_reserve)