map = []
antinodes = []
antenna = {}

def add_antinodes(n1, n2):
    global antinodes
    delta_x = n1[0] - n2[0]
    delta_y = n1[1] - n2[1]
    an1_x = n1[0] + delta_x
    an1_y = n1[1] + delta_y
    an2_x = n2[0] - delta_x
    an2_y = n2[1] - delta_y

    #print(f"Two antinodes for antenna ({n1[0],n1[1]}) and ({n2[0]},{n2[1]}): ({an1_x},{an1_y}) and ({an2_x},{an2_y})")
    if an1_x >= 0 and an1_x < len(map) and an1_y >= 0 and an1_y < len(map[0]):
        antinodes[an1_x][an1_y] = "X"
    if an2_x >= 0 and an2_x < len(map) and an2_y >= 0 and an2_y < len(map[0]):
        antinodes[an2_x][an2_y] = "X"

f = open("puzzle.input", "r")
i = 0
for line in f:
    line = line.rstrip()
    map.append(list(line))
    antinodes.append(list("."*len(line)))
    j = 0
    for c in line:
        if c != ".":
            if c not in antenna:
                antenna[c] = []
            antenna[c].append((i,j))
        j += 1
    i += 1

print(antenna)

for freq in antenna:
    nodes = antenna[freq]
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            add_antinodes(nodes[i], nodes[j])

for line in antinodes:
    print("".join(line))

sum = 0
for line in antinodes:
    sum += line.count("X")

print(sum)