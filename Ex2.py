lst= [-3,-2,-5,-9,-4,-5.1]
maximum=float(lst[0])
for i in range(len(lst)):
    if float(lst[i])>maximum : maximum=float(lst[i])
if maximum>=0. :
    print(maximum)
else:
    print("Sunt doar numere negative")