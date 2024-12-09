map = []
f = open("puzzle.input","r")

i=0
j=0
direction = ""
direction_i = 0
direction_j = 0

count = 0
for line in f:
    line = line.strip()
    if ">" in line or "<" in line or "^" in line or "v" in line:
        i = count
        if ">" in line:
            direction = ">"
            direction_i = 0
            direction_j = 1
        if "v" in line:
            direction = "v"
            direction_i = 1
            direction_j = 0
        if "<" in line:
            direction = "<"
            direction_i = 0
            direction_j = -1
        if "^" in line:
            direction = "^"
            direction_i = -1
            direction_j = 0
        j = line.index(direction)
        print(f"STARTING: {i},{j},{direction}")
    map.append(list(line.rstrip()))
    count += 1

# i,j is starting position and direction is the direction
map[i][j] = "X"

# while its on the map...
while i >= 0 and i < len(map[0]) and j >= 0 and j < len(map):
    new_i = i + direction_i
    new_j = j + direction_j
    if new_i < 0 or new_j < 0 or new_i == len(map[0]) or new_j == len(map):
        # off the map
        break
    if map[new_i][new_j] == "#":
        # hit an obstruction, turn right
        if direction_i == 1:
            direction_i = 0
            direction_j = -1
        elif direction_i == -1:
            direction_i = 0
            direction_j = 1
        elif direction_j == 1:
            direction_i = 1
            direction_j = 0
        elif direction_j == -1:
            direction_i = -1
            direction_j = 0
    else:
        i = new_i
        j = new_j
        map[i][j] = "X"

sum = 0
for line in map:
    sum += line.count("X")

for line in map:
    print("".join(line))

print(sum)