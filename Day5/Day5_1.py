import re

file = open("Day5/Day5.txt", "r")
lines = file.readlines()
file.close()

cond1 = re.compile(r"([aeiou].*){3,}")
cond2 = re.compile(r"(\w)\1+")
cond3 = re.compile(r"(ab|cd|pq|xy)")

nice = 0
for line in lines:
    if cond1.search(line) and cond2.search(line) and not cond3.search(line):
        nice += 1

print("nice", nice)
print("naughty", len(lines) - nice)
print("all", len(lines))