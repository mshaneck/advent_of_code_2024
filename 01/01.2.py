puzzle_input = None

list1 = []
list2 = []

with open("./puzzle.input", "r") as f:
    for line in f:
        a,b = line.split()
        list1.append(int(a))
        list2.append(int(b))

similarity = 0
for a in list1:
    similarity += a*list2.count(a)

print(similarity)