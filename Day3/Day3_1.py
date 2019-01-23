import re

file = open("Day3/Day3.txt", "r")
lines = file.readlines()
file.close()

line = lines[0]

locations = [(0, 0)]
x = 0
y = 0
presents = 1
for chara in line:
    if chara == "^":
        y -= 1
    elif chara == ">":
        x += 1
    elif chara == "v":
        y += 1
    else:
        x -= 1

    if not (x, y) in locations:
        locations.append((x, y))
        presents += 1

print(presents)