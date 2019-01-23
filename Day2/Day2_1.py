import re

file = open("Day2/Day2.txt", "r")
lines = file.readlines()
file.close()

regex = re.compile(r"\d+")

sume = 0
for line in lines:
    numbers = regex.findall(line)
    numbers = [int(i) for i in numbers]

    side1 = numbers[0] * numbers[1]
    side2 = numbers[1] * numbers[2]
    side3 = numbers[0] * numbers[2]

    small = min(side1, side2, side3)
    sume += 2 * side1 + 2 * side2 + 2 * side3 + small

print(sume)