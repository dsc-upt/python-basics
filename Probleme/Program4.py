team = []
reserves = []

print ("Add 5 players: ")
for i in range (5):
    player = {"Name": "0", "Age": 0, "Number": 0}
    player["Name"] = input("Name: ")
    player["Age"] = int (input("Age: "))
    player["Number"] = int (input("Number: "))
    team.append(player)

print("Add 3 reserves: ")
for i in range (3):
    player = {"Name": "0", "Age": 0, "Number": 0}
    player["Name"] = input("Name: ")
    player["Age"] = int (input("Age: "))
    player["Number"] = int (input("Number: "))
    reserves.append(player)

print(team)
print(reserves)

pl1 = input("Choose player: ")
rs1 = input("Choose reserve: ")

i = 0
for element in team:
    if element["Name"] == pl1:
        poz1 = i
    i+=1

i = 0
for element in reserves:
    if element["Name"] == rs1:
        poz2 = i
    i+=1

team[poz1]["Name"], reserves[poz2]["Name"] = reserves[poz2]["Name"], team[poz1]["Name"]
team[poz1]["Age"], reserves[poz2]["Age"] = reserves[poz2]["Age"], team[poz1]["Age"]
team[poz1]["Number"], reserves[poz2]["Number"] = reserves[poz2]["Number"], team[poz1]["Number"]

print(team)
print (reserves)