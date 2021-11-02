players = []
reserve_players = []


def print_players(player_list, size):
    print("\n")
    for j in range(size):
        print(player_list[j])
    print("\n")


print("Please add 5 players to the team (name, age, number, position): ")
for i in range(5):
    print(f"Please provide information for player {i+1}: ")
    person = {}
    name = input("Name: ")
    person["name"] = name
    age = int(input("Age: "))
    person["age"] = age
    number = int(input("Number: "))
    person["number"] = number
    position = input("Position: ")
    person["position"] = position
    players.append(person)
    print("\n")

print("\nPlease add 3 players to the reserve team (name, age, number, position): ")

for i in range(3):
    person = {}
    print(f"Please provide information for player {i + 1}: ")
    name = input("Name: ")
    person["name"] = name
    age = int(input("Age: "))
    person["age"] = age
    number = int(input("Number: "))
    person["number"] = number
    position = input("Position: ")
    person["position"] = position
    reserve_players.append(person)
    print("\n")

print_players(players, 5)
print_players(reserve_players, 3)

print("Please provide the names for the players to be swapped: ")
name1 = input("Provide first name (Player in team):")
name2 = input("Provide second name (Player in reserve team): ")
player1 = {}
player2 = {}
index_player1 = -1
index_player2 = -1
for i in range(5):
    if players[i]["name"] == name1:
        player1 = players[i]
        index_player1 = i
        break
for i in range(3):
    if reserve_players[i]["name"] == name2:
        player2 = reserve_players[i]
        index_player2 = i
        break
if index_player2 < 0 or index_player1 < 0:
    print("Numele introdus nu exista in baza de date")
else:
    players[index_player1] = player2
    reserve_players[index_player2] = player1

print_players(players, 5)
print_players(reserve_players, 3)
