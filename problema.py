nr_jucatori = 5
nr_rezerve = 3
players = [dict() for number in range(nr_jucatori)]
rezerve = [dict() for number in range(nr_rezerve)]

for i in range(nr_jucatori) :
    nume=input("input player name:")
    number=int(input("input player number:"))
    age=int(input("input player age:"))
    players[i].update({"name":nume, "number":number,"age":age})

for i in range(nr_rezerve) :
    nume=input("input reserve name:")
    number=int(input("input reserve number:"))
    age=int(input("input reserve age:"))
    rezerve[i].update({"name":nume, "number":number,"age":age})

print(players)
print(rezerve)

s1 = input("player name:")
s2 = input("reserve name:")

for i in range(nr_jucatori) :
    if players[i].get("name")==s1:
        for j in range(nr_rezerve):
            if rezerve[j].get("name")==s2:
                temp = rezerve[j]
                rezerve[j]=players[i]
                players[i]=temp
                break

print(players)
print(rezerve)