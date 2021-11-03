mylist = [1, 2, 3.14, -4, 56]
maximum = mylist[0]

for el in mylist:
    if el > 0 and el > maximum:
        maximum = el

print(maximum)

    