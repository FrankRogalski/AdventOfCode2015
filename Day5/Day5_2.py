import re

file = open("Day5/Day5.txt", "r")
lines = file.readlines()
file.close()

cond1 = re.compile(r"(\w\w).*\1")
cond2 = re.compile(r"(\w).\1")

nice = 0
for line in lines:
    if cond1.search(line) and cond2.search(line):
        nice += 1

print("nice", nice)
print("naughty", len(lines) - nice)
print("all", len(lines))