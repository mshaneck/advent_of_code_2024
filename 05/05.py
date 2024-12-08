
f = open("puzzle.input", "r")

rules = {}

sum = 0

for line in f:
    if "|" in line:
        (first, second) = line.rstrip().split("|")
        if first not in rules:
            rules[first] = []
        rules[first].append(second)
        
    if "," in line:
        pages = line.rstrip().split(",")
        valid = True
        for i,page in enumerate(pages):
            if page in rules:
                for seconds in rules[page]:
                    if seconds in pages[0:i]:
                        # rule is violated
                        valid = False
        if valid: 
            sum += int(pages[(len(pages)-1)//2])

print(sum)