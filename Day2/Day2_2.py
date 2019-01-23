import re

file = open("Day2/Day2.txt", "r")
lines = file.readlines()
file.close()

regex = re.compile(r"\d+")

sume = 0
for line in lines:
    numbers = regex.findall(line)
    numbers = [int(i) for i in numbers]
    numbers.sort()
    feet = numbers[0] * numbers[1] * numbers[2]
    length = (numbers[0] << 1) + (numbers[1] << 1)
    sume += length + feet

print(sume)