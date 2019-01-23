file = open("Day1/Day1.txt", "r")
lines = file.readlines()
file.close()

line = lines[0]

floor = 0
for chara in line:
    if chara == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
