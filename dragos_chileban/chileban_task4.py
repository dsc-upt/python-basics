startingLineup = [{'name': 'De gea', 'age': 30, 'number': 1, 'position': 'gk', 'team': 'mun'}, {'name': 'mbappe', 'age': 23, 'number': 10, 'position': 'st', 'team': 
'psg'}]
Substitutes = [{'name': 'Messi', 'age': 33, 'number': 33, 'position': 'st', 'team': 'psg'}, {'name': 'Ronaldo', 'age': 35, 'number': 7, 'position': 'st', 'team': 
'mun'}]

def add_players():
    for i in range(5):
        players_dict = {}
        name = input("Please enter the player's name: ")
        players_dict["name"] = name
        age = int(input("Please enter the player's age: "))
        players_dict["age"] = age
        number = int(input("Please enter the player's number: "))
        players_dict["number"] = number
        position = input("Please enter the player's position: ")
        players_dict['position'] = position
        team = input("Please enter the player's team: ")
        players_dict['team'] = team
        players_dict_copy = players_dict.copy()
        startingLineup.append(players_dict_copy)

def add_substitutes():
    for i in range(3):
        substitutes_dict = {}
        name = input("Please enter the player's name: ")
        substitutes_dict["name"] = name
        age = int(input("Please enter the player's age: "))
        substitutes_dict["age"] = age
        number = int(input("Please enter the player's number: "))
        substitutes_dict["number"] = number
        position = input("Please enter the player's position: ")
        substitutes_dict['position'] = position
        team = input("Please enter the player's team: ")
        substitutes_dict['team'] = team
        substitutes_dict_copy = substitutes_dict.copy()
        Substitutes.append(substitutes_dict_copy)

def make_change():
    firstTeamName = input("Please enter the name of the player you want to change: ")
    subName = input("Please enter the name of the sub you want to change the player with: ")
    for player in startingLineup:
        if player['name'] == firstTeamName:
            startingLineup.remove(player)
            Substitutes.append(player)

    for player in Substitutes:
        if player['name'] == subName:
            Substitutes.remove(player)
            startingLineup.append(player)


add_players()
add_substitutes()
print(startingLineup)
print(Substitutes)
make_change()
print(startingLineup)
print(Substitutes)