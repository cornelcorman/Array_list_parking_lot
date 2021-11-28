# parking lot
p     = ["Mercedes",  None, "BMW",  None,  "KIA", "KIA", "BMW" ]
# index           0,    1,     2,     3,      4,    5,    6 
# HW 1 - calculate / print statistics: As resolt :  # Mercedes - 1  # BMW - 2  # KIA - 1
user_car_brend = input("input your brand ?")
user_park_index = int(input("What place ?"))
if p[user_park_index] == None:
    print("OK, You can park there !")
    p[user_park_index] = user_car_brend
else:
    print("This place is occied !")


# free / total
total = len ( p )
free = 0
mercedes = 0
bmw      = 0
kia      = 0
for i in range(len(p)):
    if p[i] == None:
         free = free + 1
    if p[i] == "Mercedes":
         mercedes = mercedes + 1
    if p[i] == "BMW":
         bmw = bmw + 1
    if p[i] == "KIA":
         kia = kia + 1
print("Parkink (free / total): ", free, "/", total, "places")
for i in range(len(p)):
    print(i, p[i])
print("Cars brend in parking lot: ","\n", "Mercedes: ", mercedes, "\n", "BMW:      ", bmw, "\n", "KIA:      ", kia)





