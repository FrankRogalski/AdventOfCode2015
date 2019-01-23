import re

file = open("Day6/Day6.txt", "r")
lines = file.readlines()
file.close()

grid = [[False for x in range(1000)] for y in range(1000)] 

valueGetter = re.compile(r"(toggle|turn (on|off)) (\d+)\,(\d+) through (\d+)\,(\d+)")
for line in lines:
    values = valueGetter.findall(line)
    values = values[0]
    for x in range(int(values[2]), int(values[4]) + 1):
        for y in range(int(values[3]), int(values[5]) + 1):
            if values[1] == "":
                grid[x][y] = not grid[x][y]
            elif values[1] == "on":
                grid[x][y] = True
            else:
                grid[x][y] = False

on = 0
for x in range(1000):
    for y in range(1000):
        if grid[x][y]:
            on += 1
print(on)