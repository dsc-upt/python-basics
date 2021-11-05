players=[]
for k in range(5):
    jucatork={"Name": 0, "Age": 0,"Number": 0}
    name=input("Numele jucatorului:")
    age=int(input("Varsta jucatorului:"))
    number=int(input("Numarul jucatorului:"))
    jucatork["Name"]=name
    jucatork["Age"]=age
    jucatork["Number"]=number
    players.append(jucatork)
print(players)
reserve=[]
for k in range(3):
    jucatork={"Name": 0, "Age": 0,"Number": 0}
    name=input("Numele jucatorului:")
    age=int(input("Varsta jucatorului:"))
    number=int(input("Numarul jucatorului:"))
    jucatork["Name"]=name
    jucatork["Age"]=age
    jucatork["Number"]=number
    reserve.append(jucatork)
print(reserve)
p1=input()
p2=input()
for k in range(5):
    if players[k]["Name"]==p1:
        p12=players[k]
        players.pop(k)
for k in range(3):
    if reserve[k]["Name"]==p2:
        p21=reserve[k]
        reserve.pop(k)
aux=p12
p12=p21
p21=aux
print(players)
print(reserve)
