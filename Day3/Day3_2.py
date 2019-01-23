import re

file = open("Day3/Day3.txt", "r")
lines = file.readlines()
file.close()

line = lines[0]

locations = [[0, 0]]
location_santa = [0, 0]
location_robo = [0, 0]
presents = 1
robo = False
for chara in line:
    if not robo:
        if chara == "^":
            location_santa[1] -= 1
        elif chara == ">":
            location_santa[0] += 1
        elif chara == "v":
            location_santa[1] += 1
        else:
            location_santa[0] -= 1

        if not location_santa in locations:
            locations.append(location_santa.copy())
            presents += 1
    else:
        if chara == "^":
            location_robo[1] -= 1
        elif chara == ">":
            location_robo[0] += 1
        elif chara == "v":
            location_robo[1] += 1
        else:
            location_robo[0] -= 1

        if not location_robo in locations:
            locations.append(location_robo.copy())
            presents += 1

    robo = not robo
    

print(presents)