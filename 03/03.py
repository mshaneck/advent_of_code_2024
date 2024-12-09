import re

f = open("puzzle.input", "r")

line = f.read()
matches = re.findall("mul\([0-9]+,[0-9]+\)", line)

sum = 0
for match in matches:
    numbers = match[4:-1].split(",")
    sum  += int(numbers[0]) * int(numbers[1])

print(sum)

