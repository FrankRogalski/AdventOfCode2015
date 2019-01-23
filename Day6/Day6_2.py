import re

file = open("Day6/Day6.txt", "r")
lines = file.readlines()
file.close()

grid = [[0 for x in range(1000)] for y in range(1000)] 

valueGetter = re.compile(r"(toggle|turn (on|off)) (\d+)\,(\d+) through (\d+)\,(\d+)")
for line in lines:
    values = valueGetter.findall(line)
    values = values[0]
    for x in range(int(values[2]), int(values[4]) + 1):
        for y in range(int(values[3]), int(values[5]) + 1):
            if values[1] == "":
                grid[x][y] += 2
            elif values[1] == "on":
                grid[x][y] += 1
            elif grid[x][y] > 0:
                grid[x][y] -= 1

brightness = 0
for x in range(1000):
    for y in range(1000):
            brightness += grid[x][y]
print(brightness)