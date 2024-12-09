import re

f = open("puzzle.input", "r")

line = f.read()
#matches = re.findall("mul\([0-9]+,[0-9]+\)", line)
matches = re.findall("(don[']t\(\)|do\(\)|mul\([0-9]+,[0-9]+\))", line)

sum = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        numbers = match[4:-1].split(",")
        sum  += int(numbers[0]) * int(numbers[1])

print(sum)

