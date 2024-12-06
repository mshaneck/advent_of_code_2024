
puzzle_input = None

list1 = []
list2 = []

with open("./puzzle.input", "r") as f:
    for line in f:
        a,b = line.split()
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

distance = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(distance)

